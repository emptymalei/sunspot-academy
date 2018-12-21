import axios from 'axios'

let $axios = axios.create({
  baseURL: '/api/',
  timeout: 5000,
  headers: {'Content-Type': 'application/json'}
})

// Request Interceptor
$axios.interceptors.request.use(function (config) {
  config.headers['Authorization'] = 'Fake Token'
  return config
})

// Response Interceptor to handle and log errors
$axios.interceptors.response.use(function (response) {
  return response
}, function (error) {
  // Handle Error
  console.log(error)
  return Promise.reject(error)
})

export default {

  fetchFlow () {
    return $axios.get(`flow`)
      .then(response => response.data)
  },

  fetchFlowByID (FlowId) {
    console.log(`flow/id/` + FlowId)
    return $axios.get(`flow/id/` + FlowId)
      .then(response => response.data)
  },

  fetchRandomFlow () {
    return $axios.get(`flow/random`)
      .then(response => response.data)
  },

  fetchRecentFlow () {
    return $axios.get(`flow/recent/2`)
      .then(response => response.data)
  },

  fetchResource () {
    return $axios.get(`resource/xxx`)
      .then(response => response.data)
  },

  fetchSecureResource () {
    return $axios.get(`secure-resource/zzz`)
      .then(response => response.data)
  },

  postFlow (author, content) {
    $axios.post(`flow`, {
      author: author,
      content: content
    })
  }

}
