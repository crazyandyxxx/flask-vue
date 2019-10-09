
<template>
  <div id="app" @mousemove="moveEvent" @click="moveEvent">
    <!--<keep-alive>
    <router-view v-if="$route.meta.keepAlive"></router-view>
    </keep-alive>
    <router-view v-if="!$route.meta.keepAlive"></router-view>-->
    <Header></Header>
    <router-view ></router-view>
  </div>
</template>

<script>
import Header from '@/components/Navigation.vue'
export default {
  name: 'App',
  components: {
    Header
  },
  data () {
    return {
      timmer: null
    }
  },
  methods: {
    moveEvent () {
      let path = ['/login']
      if (!path.includes(this.$route.path)) {
        clearTimeout(this.timmer)
        this.init()
      }
    },
    init () {
      this.timmer = setTimeout(() => {
        localStorage.removeItem('Authorization', '')
        localStorage.clear()
        this.$router.push({
          path: '/login'
        })
      }, 30 * 60 * 1000)
    }
  }

}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  padding: 0px;
  margin: 0px;
  height: 100%;
}
</style>
