<template>
  <div class="sidebar">
    <!-- Tip Tabs -->
    <!-- a side-bar -->
    <div class="sidebar-box" v-show="isSidebarShown" @mouseleave="hideSidebar">
      <ul>
        <li><img src="@/assets/accout.png" alt="Account" /></li>
        <li><a href="#" @click.prevent="ChangeComponent('login')">Account</a></li>
        <li><img src="@/assets/fati.png" alt="Account" /></li>
        <li><a href="#" @click.prevent="ChangeComponent('charts')">Fatiguest</a></li>
        <li><img src="@/assets/face.png" alt="Account" /></li>
        <li><a href="#" @click.prevent="ChangeComponent('face')">Facogn</a></li>
        <li><img src="@/assets/about.png" alt="Account" /></li>
        <li><a href="#" @click.prevent="ChangeComponent('about')">About</a></li>
      </ul>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
//import axios from "axios";
export default {
  name: 'SideBar',
  data () {
  return {
    isSidebarShown: true
  }
  },
  setup(props, context){
    const isSidebarShown = ref(false)

    function showSidebar() {
      isSidebarShown.value = true
    }

    function hideSidebar() {
      isSidebarShown.value = true
    }

    const ChangeComponent = (component) => {
      context.emit("ChangeComponent", component);
      //console.log(component)
    }

    return {
      showSidebar,
      hideSidebar,
      ChangeComponent
    }


  }
 
}
</script>

<style scoped>
.sidebar {
position: fixed;
right: 0;
top: 0;
bottom: 0;
width: 5%;
background-color: #f5f5f5;
overflow: hidden;
box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
display: flex;
flex-direction: column;
justify-content: center;
transition: right 0.3s ease-in-out;
}

.sidebar-box ul {
list-style: none;
margin-top: 0;
padding: 0;
display: flex;
flex-direction: column;
justify-content: space-around;
height: 100%;
}

.sidebar-box li {
display: flex;
flex-direction: column;
align-items: center; /* Horizontally center the items */
}

.sidebar-box li a {
display: block;
width: 100%;
height: 60px;
text-align: center;
line-height: 60px;
color: #333;
text-decoration: none;
margin-top: 0;
background-color: rgba(255, 255, 255, 0); /* Set the background color to transparent */
}

.sidebar-box li img {
max-width: 50px;
max-height: 50px;
margin-bottom: -8px;
}

.sidebar-box li a:hover {
background-color: #f5f5f5; /* Hover color, change as needed */
}
</style>




