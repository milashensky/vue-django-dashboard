import Vue from 'vue'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'
import routes from './routes/routes.js'
import App from "./App";

const router = new VueRouter({
    routes,
});


function getCookie(name){
    let re = new RegExp(name + "=([^;]+)"),
        value = re.exec(document.cookie);
    return (value != null) ? unescape(value[1]) : null;
 }

Vue.use(VueRouter);
Vue.use(VueResource);
Vue.http.options.headers = {'X-CSRFToken': getCookie('csrftoken')}

new Vue({
    el: "#app",
    render: h => h(App),
    router,
    data: {
    },
});
