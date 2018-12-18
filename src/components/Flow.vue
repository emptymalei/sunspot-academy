<template>
  <div class="flow">
    <h2 class="title">
      Sunspots
    </h2>
    <div v-for="r in flow" :key="r.datetime" style="margin-top:1em;">
      <div class="card">
        <header class="card-header is-vcentered">
          <p class="card-header-title">
            Random Sunspot
          </p>
          <a href="" @click.prevent="fetchRandomFlow" class="button is-dark is-outlined" style="margin-top: 0.4em;margin-right: 0.5em;">Fetch Another Random Sunspot</a>
        </header>
        <div class="card-content">
          <div class="content">
            {{ r.content }}
          </div>
        </div>
        <footer class="card-footer">
          <span class="card-footer-item">@{{ r.author }}</span>
          <span href="#" class="card-footer-item"><time>{{ r.datetime }}</time></span>
        </footer>
      </div>
    </div>
    <div class="card">
        <header class="card-header is-vcentered">
          <p class="card-header-title">
            Recent Sunspots
          </p>
        </header>
        <div v-for="r in recent.slice().reverse()" :key="r.datetime">
          <div class="card-content">
            <div class="content">
              {{ r.content }}
            </div>
          </div>
          <footer class="card-footer" style="border-bottom:1px solid #dbdbdb;">
            <span class="card-footer-item">@{{ r.author }}</span>
            <span href="#" class="card-footer-item"><time>{{ r.datetime }}</time></span>
          </footer>
      </div>
    </div>

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
            <b-input name="name" placeholder="Display ID" v-model="oneflow.author" expanded></b-input>
            <span class='warning'>This will appear alongside the content.</span>
          </b-field>
          <b-field horizontal label="Sunspot">
            <b-input type="textarea" v-model="oneflow.content"></b-input>
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
