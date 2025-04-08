import { createApp } from 'vue'
import ECharts from 'vue-echarts';
import App from './App.vue';
import 'echarts';
import '@/assets/font/font.css';
import '@/assets/font/mvboli.css';

/*
Object.defineProperty(Vue.prototype, 'flag', {
    value: true
  });
*/

createApp(App)
  .component('ECharts', ECharts)
  .mount('#app');


