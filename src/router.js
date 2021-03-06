import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import About from './views/About.vue'
import Random from './views/Random.vue'
import ID from './views/ID.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/about',
      name: 'about',
      component: About
    },
    {
      path: '/random',
      name: 'random',
      component: Random
    },
    {
      path: '/id',
      name: 'id',
      component: ID,
      props: (route) => ({
        id: route.query.id
      })
    }
  ]
})
