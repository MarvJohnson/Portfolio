import { createApp } from 'vue';
import App from './App.vue';
import { library } from '@fortawesome/fontawesome-svg-core';
import {
  faHtml5,
  faCss3Alt,
  faNodeJs,
  faGithub,
  faLinkedin
} from '@fortawesome/free-brands-svg-icons';
// import { far } from '@fortawesome/free-regular-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

library.add(faHtml5, faCss3Alt, faNodeJs, faGithub, faLinkedin);

createApp(App).component('font-awesome-icon', FontAwesomeIcon).mount('#app');
