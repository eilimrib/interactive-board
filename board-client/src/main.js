import { createApp } from 'vue';
import App from './App.vue';
import axios from 'axios';
import VueAxios from 'vue-axios';
import './styles/app.css';

const app = createApp(App)
app.use(VueAxios, axios)
app.mount('#app')