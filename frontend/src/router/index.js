import Vue from 'vue'
import Router from 'vue-router'

const routerOptions = [
  { path: '/', component: 'Home', meta: { isLogin: true } },
  { path: '/about', component: 'About', meta: { isLogin: true } },
  { path: '*', component: 'NotFound', meta: { isLogin: true } },
  {path: '/login', component: 'Login', meta: { isLogin: false }},
  {path: '/register', component: 'Register', meta: { isLogin: false }}
]

const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
  }
})

Vue.use(Router)
export default new Router({
  routes,
  mode: 'history'
})
