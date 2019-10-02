<template>
<el-form ref="AccountFrom" :model="account" :rules="rules" label-position="left" label-width="0px" class="demo-ruleForm login-container">
<h3 class="title">系统登录</h3>
<el-form-item prop="username">
<el-input type="text" v-model="account.username" auto-complete="off" placeholder="账号"></el-input>
</el-form-item>
    <el-form-item prop="pwd">
      <el-input type="password" v-model="account.pwd" auto-complete="off" placeholder="密码"></el-input>
    </el-form-item>
    <el-form-item style="width:100%;">
      <el-button type="primary" style="width:100%;" @click="register">注册</el-button>
    </el-form-item>
  </el-form>
</template>
<script>
import axios from 'axios'
export default {
  name: 'register',
  data () {
    return {
      logining: false,
      account: {
        username: '',
        pwd: ''
      },
      rules: {
        username: [
          {required: true, message: '请输入账号', trigger: 'blur'}
          // { validator: validaePass }
        ],
        pwd: [
          {required: true, message: '请输入密码', trigger: 'blur'}
          // { validator: validaePass2 }
        ]
      }
    }
  },
  methods: {
    register () {
      const path = `http://localhost:6015/auth/register`
      axios.post(path, {
        username: this.account.username,
        password: this.account.pwd
      })
        .then(function (res) {

        })
        .catch(function (error) {
          console.log(error)
        })
    }
  }
}
</script>
<style>
  body{
    background: #DFE9FB;
  }
  .login-container{
    width:350px;
    margin-left:35%;
  }
</style>
