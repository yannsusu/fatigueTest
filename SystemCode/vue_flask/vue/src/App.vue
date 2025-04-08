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
      <FaceRecognition id="facerecognition"
        v-if="showcomponent === 'face'"></FaceRecognition>
      <about id="about"
        v-if="showcomponent === 'about'"></about>  
    </div>
      <SideBar @ChangeComponent="ChangeComponent" ></SideBar>
      <logo></logo>
  </div>
</template>

<script>
import FlipClock from './components/FlipClock.vue'
import SideBar from './components/sidebar.vue'
import Login from './components/login.vue'
import Charts from './components/Charts.vue'
import FaceRecognition from './components/FaceRecognition.vue'
import logo from './components/logo.vue'
import about from  './components/about.vue'
import { ref, watch } from "vue";
//import axios from 'axios';

export default { 
  // eslint-disable-next-line vue/no-unused-components
  components: { FlipClock, SideBar, Login, Charts, FaceRecognition, logo,about},
  name: 'App',

  setup(){
    let showcomponent = ref("login");
    let islogin = ref(true);

    const ChangeComponent = (component) => {
      showcomponent.value = component;
      console.log(showcomponent)
    };

    watch(
      () => showcomponent.value,
    );

    return {
      showcomponent,
      ChangeComponent,
      islogin
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
