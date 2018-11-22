import Layout from '../components/Layout.vue'
import Dashboard from '../pages/Dashboard.vue'
import Home from '../pages/Home.vue'
import Item from '../pages/Item.vue'

export default[
    {
        path: "/",
        component: Layout,
        redirect: "/dashboard",
        children: [
            {
                path: "dashboard",
                name: "Dashboard",
                isNav: true,
                component: Dashboard
            },
            {
                path: "home",
                name: "Home",
                isNav: true,
                component: Home
            },
            {
                path: "item/:id",
                props: true,
                name: "Item Detail",
                isNav: false,
                component: Item
            },
        ]
    }
]
