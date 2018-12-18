<template>
  <div class="container is-fluid home">
    <div class="columns">
      <div class="column is-one-fifth">
        <Introduction msg="The Sunspot"/>
      </div>
      <div class="column">
        <Flow/>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Introduction from '@/components/Introduction.vue'
import Flow from '@/components/Flow.vue'

export default {
  name: 'home',
  components: {
    Introduction,
    Flow
  }
}
</script>

<style lang="scss">

</style>
