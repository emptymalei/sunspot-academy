<template>
  <div class="about container" style="text-align:left;">

    <h1 class="title has-text-centered">About</h1>

    <section class="container" style="line-height:2em;">
    <div class="notification is-warning">
      <p style="margin-bottom:1em;">
        We do not track you. We will make it as transparent as possible. First and foremost, we promise you that every line of the code is open-source. Secondly, we are using an automatic pipeline from GitHub to Heroku. What you see in the GitHub repo is what is being used for the live website.
      </p>
    <p style="margin-bottom:1em;">
      Here is how the website works. The sunspot is powered by Flask and Vue.js. The frontend is connected to the backend through flask APIs. The API is coded with Flask restplus. Whenever you load the page, a request will be sent to the backend to retrieve the content. The frontend is then rendered by vue.js.</p>
      <p>That being said, you could also write your own webpage or app using our API. However, we are running on a crappy server. We kindly ask you to be nice to our APIs.
        </p>
    </div>
    </section>

  </div>
</template>

<style lang="scss">
</style>
