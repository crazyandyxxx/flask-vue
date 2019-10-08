<template>
  <el-container direction="vertical">
    <el-header>
    <Header/>
    </el-header>
    <el-main>
    <router-view/>
    </el-main>
  </el-container>
</template>

<script>
import Header from '@/components/Navigation.vue'
export default {
  name: 'App',
  components: {
    Header
  }
}
</script>

<style>
.el-container {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  padding: 0px;
  margin: 0px;
  height: 100%;
  width: 900px;
}
</style>
