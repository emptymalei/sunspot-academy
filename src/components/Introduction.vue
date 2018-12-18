<template>
  <div class="hello" style="text-align:left;margin-top:4em;">
    <h1 class="subtitle">{{ msg }}</h1>
    <p>
       Anyone can release the dark side of the mind
    </p>
    <p>
      It's like meditation: No one should be scared of the dark side of the mind.
    </p>
    <p>
      One more thing, we do not track you.
    </p>

  </div>
</template>

<script>
export default {
  name: 'Introduction',
  props: {
    msg: String
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
