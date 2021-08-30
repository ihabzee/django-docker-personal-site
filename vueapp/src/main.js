import Vue from 'vue'
import App from './App.vue'
import routes from './routes'
import VueRouter from 'vue-router'
Vue.use(VueRouter)

Vue.config.productionTip = true

const router = new VueRouter({ mode: 'history', routes,   linkActiveClass: "active", // active class for non-exact links.
linkExactActiveClass: "active"  });
new Vue({
  router,
  render: h => h(App),
}).$mount('#app')


