import { createApp } from 'vue';
import { createVuetify } from 'vuetify'
import App from './App.vue';
import router from './router';
import 'vuetify/styles';
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
  components,
  directives,
})


createApp(App).use(vuetify).use(router).mount('#app')