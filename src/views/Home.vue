<template>
  <div class="container is-fluid home">
    <div class="columns">
      <div class="column">
        <Flow/>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Flow from '@/components/Flow.vue'

export default {
  name: 'home',
  components: {
    Flow
  }
}
</script>

<style lang="scss">

</style>
