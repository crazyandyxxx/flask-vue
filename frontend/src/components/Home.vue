<template>
<div>
<p>Home page</p>
<p>Random number from backend: {{ randomNumber }}</p>
<el-button type="primary" round @click="getRandom">New random number</el-button>
</div>

</template>
<script>
import axios from 'axios'
export default {
  data () {
    return {
      randomNumber: 0
    }
  },

  methods: {
    getRandomInt (min, max) {
      min = Math.ceil(min)
      max = Math.floor(max)
      return Math.floor(Math.random() * (max - min + 1)) + min
    },

    getRandom () {
      this.randomNumber = this.getRandomFromBackend()
    },

    getRandomFromBackend () {
      const path = `http://localhost:6015/api/random`
      axios.get(path)
        .then(response => {
          this.randomNumber = response.data.randomNumber
        })
        .catch(error => {
          console.log(error)
        })
    }

  },

  created () {
    this.getRandom()
  }
}

</script>
