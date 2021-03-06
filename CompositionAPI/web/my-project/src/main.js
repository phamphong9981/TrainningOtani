import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import VueCompositionAPI from '@vue/composition-api'
import mitt from 'mitt';   
import VueRouter from 'vue-router'
import router from "./router/router.js"
Vue.use(VueRouter)               
const emitter = mitt();                   
Vue.use(VueCompositionAPI)
Vue.config.productionTip = false
new Vue({
  vuetify,
  emitter,
  router,
  render: h => h(App)
}).$mount('#app')
