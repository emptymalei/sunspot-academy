<template>
  <div class="about container" style="text-align:left;">
    <section class="container" style="line-height:2em;">
    <div class="notification is-warning">
      <h1 class="title has-text-centered">About Us</h1>
    <p>
    We are a group of people trained as scientists. However, the further we walked down into this path, the more we felt we are all simply tiny, vulnerable pieces of the giant machine of knowledge production. As mentioned in the movie Blade Runner 2049, “every civilization was built off the back of a disposable workforce ”. Science, the most intellectually intensive part of modern civilization, consumes our lives faster than any other parts.
    </p>
    <p>
    We were attracted by the promise that one day our names will be remembered forever by history, only to find that a vast majority of us are doomed. Ashes to ashes, and dust to dust after our sacrifice for Athena. Because forgetting is the way to science. Scientists constantly discover, forget, and then rediscover patterns, in order to filter out those not invariant of time and space. When a pattern cannot be ignored anymore, its time comes and it will be fabricated into the main narrative of science forever, and the final acknowledgment all goes to the last scholar who re-discovered the pattern. All the failing and successful attempts before that will be forgotten.
    </p>

    <h1 class="title has-text-centered" style="margin-top:1em;">About the Sunspot Project </h1>

    <p>
    We are like the sunspots of the Sun. To see us, to understand our suffering, one will have to stare at the Sun. We created this website so we can hear each other’s voice, comfort each other,  such that the glory of the sun will not overshadow our vulnerability. Feel free to share. Fee safe to vent. You deserve this moment and this outlet. In humanity we unite.
    </p>

    <h1 class="title has-text-centered" style="margin-top:1em;">About the Code</h1>

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
