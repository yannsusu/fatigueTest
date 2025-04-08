<template>
  <div id="app">
    <div class="background">
      <div id="head">
        <flip-clock></flip-clock>
      </div>
      <Login id="login"
        v-if="showcomponent == 'login'"></Login>
      <Charts id="charts"
        v-if="showcomponent === 'charts'"></Charts>
    </div>
      <SideBar @ChangeComponent="ChangeComponent"></SideBar>
      <logo></logo>
      
  </div>
</template>

<script>
import FlipClock from './components/FlipClock.vue'
import SideBar from './components/sidebar.vue'
import Login from './components/login.vue'
import Charts from './components/Charts.vue'
import logo from './components/logo.vue'
import { ref, watch } from "vue";
import axios from 'axios';

export default { 
  // eslint-disable-next-line vue/no-unused-components
  components: { FlipClock, SideBar, Login, Charts,logo},
  name: 'App',

  setup(){
    let showcomponent = ref("login");

    const ChangeComponent = (component) => {
      showcomponent.value = component;
      console.log(showcomponent)
    };

   

    // axios.post('http://127.0.0.1:5000/user', {name: 'Bob', age: 30})
    // .then(response => {
    //   console.log(response.data);
    // })
    // .catch(error => {
    //   console.error(error);
    // });


    watch(
      () => showcomponent.value,
    );

    return {
      showcomponent,
      ChangeComponent,
    };
  }
}
</script>

<style>
html, body {
  height: 100%;
  margin: 0;
  padding: 0;
}
/*
body{
  background: rgb(254, 232, 253);
  z-index: -3;
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
}
*/
.background {
    background-image: url('@/assets/background.jpg');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    height: 100vh;
    opacity: 0.8;
  }

#head{
  position: relative;
  top: 15%;
  left:50%;
  transform: translate(-50%, -50%);
  /* background-color: brown; */
}


</style>
