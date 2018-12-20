<template>
  <div class="container is-fluid home">
    <div class="columns">
      <div class="column">
        <Random/>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Random from '@/components/Random.vue'

export default {
  name: 'random',
  components: {
    Random
  }
}
</script>

<style lang="scss">

</style>
