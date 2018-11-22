import Vue from 'vue'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'
import routes from './routes/routes.js'
import App from "./App";

const router = new VueRouter({
    routes,
});


Vue.use(VueRouter)
Vue.use(VueResource);

new Vue({
    el: "#app",
    render: h => h(App),
    router,
    data: {
    }
});
