// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import Vuex from 'vuex'
import axios from 'axios'
Vue.use(ElementUI)
Vue.use(Vuex)
Vue.use(axios)

Vue.config.productionTip = false

router.afterEach(route => {
  window.scroll(0, 0)
})

router.beforeEach((to, from, next) => {
  if (!to.meta.isLogin) {
    next()
  } else {
    let token = localStorage.getItem('Authorization')
    if (token == null || token === '') {
      next('/')
    } else {
      next()
    }
  }
})

axios.interceptors.request.use(
  config => {
    let token = localStorage.getItem('Authorization')
    if (token) {
      config.headers.common['token'] = token
    }
    return config
  },
  err => {
    return Promise.reject(err)
  })

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
  render: h => h(App)
})
