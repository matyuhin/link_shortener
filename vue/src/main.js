import Vue from 'vue'
import App from './App.vue'
import store from './store'
import Axios from 'axios'
import router from './router'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap-vue/dist/bootstrap-vue.css"


Vue.prototype.$http = Axios;
const token = localStorage.getItem('token')
if (token) {
  Vue.prototype.$http.defaults.headers.common['Authorization'] = token
}

Vue.config.productionTip = false

new Vue({
 router,
 store,
 render: h => h(App),
}).$mount('#app')
