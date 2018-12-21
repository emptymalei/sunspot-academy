import os
from flask import Flask, current_app, send_file

import logging

from .api import api_bp
from .client import client_bp

from flask import jsonify, request, Markup
from flask_pymongo import PyMongo

import datetime as dt


app = Flask(__name__, static_folder='../dist/static')
app.register_blueprint(api_bp)
# app.register_blueprint(client_bp)

from .config import Config
app.logger.info('>>> {}'.format(Config.FLASK_ENV))

mongo = PyMongo(app)
print(mongo.db.flow)
print(mongo.db.collection_names(include_system_collections=False) )

@app.route('/')
def index_client():
    dist_dir = current_app.config['DIST_DIR']
    entry = os.path.join(dist_dir, 'index.html')
    return send_file(entry)


@app.route('/api/flow', methods=['GET'])
def get_all_flow():
    flow = mongo.db.flow

    output = []

    for record in flow.find():
        output.append({
            'id': record.get('id'),
            'author': record.get('author'),
            'datetime': record.get('datetime'),
            'content': record.get('content')
        })


    return jsonify({'result' : output})

@app.route('/api/flow/random', defaults={'sample_size': None})
@app.route('/api/flow/random/<sample_size>', methods=['GET'])
def get_random_flow(sample_size=None):
    
    if sample_size is None:
        sample_size = 1
    else:
        sample_size = int(sample_size)

    flow = mongo.db.flow

    output = []

    for record in flow.aggregate([{'$sample': {'size': sample_size }}]):
        output.append({
            'id': record.get('id'),
            'author': record.get('author'),
            'datetime': record.get('datetime'),
            'content': record.get('content')
        })


    return jsonify({'result' : output})

@app.route('/api/flow/recent', defaults={'how_many': 1})
@app.route('/api/flow/recent/<how_many>', methods=['GET'])
def get_recent_flow(how_many=None):

    if how_many is None:
        how_many = 1
    else:
        how_many = int(how_many)

    flow = mongo.db.flow

    output = []

    for record in flow.find().sort('datetime',-1).limit(how_many):
        output.append({
            'id': record.get('id'),
            'author': record.get('author'),
            'datetime': record.get('datetime'),
            'content': record.get('content')
        })

    return jsonify({'result' : output})


@app.route('/api/flow/id/<id>', methods=['GET'])
def get_one_flow_by_id(id):
    flow = mongo.db.flow

    record = flow.find_one({'id' : id})

    if record:
        output = {
            'id': record.get('id'),
            'author': record.get('author'),
            'datetime': record.get('datetime'),
            'content': record.get('content')
        }
    else:
        output = 'No flow found'

    return jsonify({'result' : output})

@app.route('/api/flow/author/<author>', methods=['GET'])
def get_one_flow_by_author(author):
    flow = mongo.db.flow

    record = flow.find_one({'author' : author})

    if record:
        output = {
            'id': record.get('id'),
            'author': record.get('author'),
            'datetime': record.get('datetime'),
            'content': record.get('content')
        }
    else:
        output = 'No flow found'

    return jsonify({'result' : output})

@app.route('/api/flow', methods=['POST'])
def add_flow():
    flow = mongo.db.flow

    author = request.json['author']
    content = Markup.escape(request.json['content'])
    datetime = dt.datetime.now()
    flow_id = '{}_{}'.format(author,datetime.strftime("%s"))

    flow_obj_id = flow.insert({
        'author' : author, 
        'content' : content,
        'datetime': datetime,
        'id': flow_id
        })
    app.logger.info(flow_id)
    app.logger.info(content)
    new_flow = flow.find_one({'id' : flow_id})

    output = {'id' : new_flow['id'], 'content' : new_flow['content']}

    return jsonify({'result' : output})