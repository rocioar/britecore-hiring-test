<template>
  <div id="app">
    <nav-header v-once></nav-header>
    <b-container class="mt-4">
      <router-view/>
    </b-container>

  </div>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import NavHeader from './NavHeader.vue'

export default {
  name: 'App',
  components: {
    'nav-header': NavHeader
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
