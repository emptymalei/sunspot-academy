<template>
  <div id="app">
    <nav class="navbar" role="navigation" aria-label="main navigation" style="border-bottom:1px solid #bdbdbd;margin-bottom:1em;">
      <div class="navbar-brand">
        <a class="navbar-item" href="/">
            The Sunspot
        </a>
        <a role="button" class="navbar-burger burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div id="navbarBasicExample" class="navbar-menu">
        <div class="navbar-start">
          <a class="navbar-item">
            <router-link to="/">Recent</router-link>
          </a>
          <a class="navbar-item">
            <router-link to="/random">Random</router-link>
          </a>
          <a class="navbar-item">
            <router-link to="/about">About</router-link>
          </a>
        </div>

        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <a class="button is-link is-outlined">
                <a href="https://github.com/emptymalei/sunspot-academy">GitHub</a>
              </a>
            </div>
          </div>
        </div>
      </div>
    </nav>
    <router-view/>

  </div>
</template>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background: url(assets/sunspot.jpg) no-repeat center center fixed; -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
  min-height: 800px;
}
#nav {
  padding: 30px;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
#plus {
  padding: 0 20px 0 20px;
  display: inline-block;
  font-size: 50px;
  vertical-align: top;
  line-height: 100px;
}

</style>
