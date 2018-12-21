<template>
  <div class="flow">
    <article class="message is-warning">
      <div class="message-header is-warning">
        <p> Recent Sunspots</p>
      </div>
      <div class="message-body">
        <div v-for="r in recent.slice().reverse()" :key="r.datetime">
          <div class="card" style="margin-top:1em; margin-bottom:1em;">
              <header class="card-header is-vcentered">
              <p class="card-header-title">
               {{ r.author }}:
              </p>
              </header>
              <div class="card-content">
                <div class="content" v-html="markUpContent(r.content)">
                </div>
              </div>
              <footer class="card-footer" style="border-bottom:1px solid #dbdbdb;">
                <span href="#" class="card-footer-item"><time>{{ r.datetime }}</time></span>
                <span class="card-footer-item" style="overflow: hidden;display: inline-block;">Sunspot ID: <a v-bind:href="'/#/id?id='+r.id">{{ r.id }}</a></span>
              </footer>
          </div>
        </div>
      </div>
    </article>

    <p class="is-warning">{{error}}</p>
    <div class="create-flow" style="margin-top:1em;">
      <article class="message is-warning">
      <div class="message-header is-warning">
        <p class="has-text-centered">Submit Your Sunspot</p>
      </div>
      <div class="message-body">
        <p style="margin-bottom:1em;">
          Be respectful
        </p>
          <form>
          <b-field horizontal label="Author">
            <b-input name="name" placeholder="Display ID" maxlength="15" v-model="oneflow.author" expanded required></b-input>
            <span class='warning' type="is-danger">This will appear alongside the content. Do not use ; / ? : @ = & "</span>
          </b-field>
          <b-field horizontal label="Sunspot" :message="['Do not disclose personal information', 'No editing once submitted', 'create a issue if you need help: https://github.com/emptymalei/sunspot-academy/issues']">
            <b-input type="textarea" v-model="oneflow.content" maxlength="5000" required></b-input>
          </b-field>
          <b-field horizontal>
            <!-- Label left empty for spacing -->
            <p class="control">
              <button @click.prevent="postFlow" class="button is-primary" :disabled="submitButton.submitted">
                {{ submitButton.text }}
              </button>
            </p>
          </b-field>
        </form>
      </div>
      </article>
    </div>
  </div>
</template>

<script>

import $backend from '../backend'

export default {
  name: 'Flow',
  data () {
    return {
      resources: [],
      flow: [],
      recent: [],
      oneflow: {
        author: '',
        content: ''
      },
      submitButton: {
        text: 'Publish Sunspot',
        submitted: false
      },
      error: ''
    }
  },
  methods: {
    markUpContent (content) {
      return $backend.markUpContent(content)
    },
    fetchFlow () {
      $backend.fetchFlow()
        .then(responseData => {
          this.flow = responseData.result
        }).catch(error => {
          this.error = error.message
        })
    },
    fetchRandomFlow () {
      $backend.fetchRandomFlow()
        .then(responseData => {
          this.flow = responseData.result
        }).catch(error => {
          this.error = error.message
        })
    },
    fetchRecentFlow () {
      $backend.fetchRecentFlow()
        .then(responseData => {
          this.recent = responseData.result
        }).catch(error => {
          this.error = error.message
        })
    },
    postFlow () {
      if (this.oneflow.author === '' | this.oneflow.content === '') {
        this.submitButton.text = 'Finish your sunspot and submit again'
        this.submitButton.submitted = false
      } else {
        $backend.postFlow(this.oneflow.author, this.oneflow.content)
        this.oneflow.author = ''
        this.oneflow.content = ''
        this.submitButton.text = 'Submitted!'
        this.submitButton.submitted = true
        $backend.fetchRecentFlow()
          .then(responseData => {
            this.recent = responseData.result
          }).catch(error => {
            this.error = error.message
          })
      }
    }
  },
  mounted: function () {
    this.fetchRecentFlow()
    this.fetchRandomFlow()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
