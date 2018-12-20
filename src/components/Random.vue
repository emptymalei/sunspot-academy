<template>
  <div class="flow">
    <article class="message is-warning">
      <div class="message-header is-warning">
        <p>Random Sunspot</p>
      </div>
      <div class="message-body">
        <div v-for="r in flow" :key="r.datetime" style="margin-top:1em;">
          <div class="card">
            <header class="card-header is-vcentered">
              <p class="card-header-title">
                {{ r.author }}:
              </p>
            </header>
            <div class="card-content">
              <div class="content">
                {{ r.content }}
              </div>
            </div>
            <footer class="card-footer">
              <span href="#" class="card-footer-item"><time>{{ r.datetime }}</time></span>
              <span class="card-footer-item">Sunspot ID: {{ r.id }}</span>
            </footer>
          </div>

          <a href="" @click.prevent="fetchRandomFlow" class="button is-dark is-outlined" style="margin-top: 2em;">Fetch Another Random Sunspot</a>
        </div>
      </div>
    </article>
    <p class="is-warning">{{error}}</p>
  </div>
</template>

<script>

import $backend from '../backend'

export default {
  name: 'Random',
  data () {
    return {
      resources: [],
      flow: [],
      recent: [],
      oneflow: {
        author: '',
        content: ''
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
    }
  },
  mounted: function () {
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
