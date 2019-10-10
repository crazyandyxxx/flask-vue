<template>
    <el-menu
  :default-active="$route.path"
  class="el-menu-demo"
  mode="horizontal"
  background-color="#545c64"
  text-color="#fff"
  active-text-color="#ffd04b" :router="true">
  <el-menu-item index="/login">登录</el-menu-item>
  <el-submenu index="2">
    <template slot="title">我的工作台</template>
    <el-menu-item index="/about">关于</el-menu-item>
    <el-menu-item index="2-2">选项2</el-menu-item>
    <el-menu-item index="2-3">选项3</el-menu-item>
    <el-submenu index="2-4">
      <template slot="title">选项4</template>
      <el-menu-item index="2-4-1">选项1</el-menu-item>
      <el-menu-item index="2-4-2">选项2</el-menu-item>
      <el-menu-item index="2-4-3">选项3</el-menu-item>
    </el-submenu>
  </el-submenu>
  <el-menu-item index="/register" >注册</el-menu-item>
  <el-menu-item index="/">主页</el-menu-item>
  <el-menu-item index="/map">地图</el-menu-item>
</el-menu>
</template>

<script>
export default {
  name: 'Header',
  data () {
    return {
    }
  }
}
</script>
