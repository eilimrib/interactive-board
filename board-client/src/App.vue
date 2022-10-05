<template>
  <div id="app">
    <BoardCards />
  </div>
</template>

<script>
import BoardCards from './components/BoardCards.vue'

export default {
  name: 'App',
  components: {
    BoardCards,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
