<template>
  <div class="flow">
    <article class="message is-warning">
      <div class="message-header is-warning">
        <p>Sunspot</p>
      </div>
      <div class="message-body">
        <div style="margin-top:1em;">
          <div class="card">
            <header class="card-header is-vcentered">
              <p class="card-header-title">
                {{ flow.author }}:
              </p>
            </header>
            <div class="card-content">
              <div class="content">
                {{ flow.content }}
              </div>
            </div>
            <footer class="card-footer">
              <span href="#" class="card-footer-item"><time>{{ flow.datetime }}</time></span>
              <span class="card-footer-item">Sunspot ID: <a v-bind:href="'/#/id?id='+ flow.id">{{ flow.id }}</a></span>
            </footer>
          </div>
        </div>
      </div>
    </article>
    <p class="is-warning">{{error}}</p>
  </div>
</template>

<script>

import $backend from '../backend'

export default {
  name: 'ID',
  data () {
    return {
      resources: [],
      flow: [],
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
    fetchFlowByID () {
      $backend.fetchFlowByID(this.$route.query.id)
        .then(responseData => {
          this.flow = responseData.result
        }).catch(error => {
          this.error = error.message
        })
    }
  },
  mounted: function () {
    this.fetchFlowByID()
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
