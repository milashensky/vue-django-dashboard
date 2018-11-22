<template lang="html">
    <ul>
        <li v-for="item in navItems" :class="(item.name == $route.name ? 'active' : '')">
            <router-link :to="{name: item.name}">{{ item.name }}</router-link>
        </li>
         <slot></slot>
    </ul>
</template>

<script>
import routes from '../../routes/routes.js'
export default {
    computed: {
        navItems: function() {
            let flat = (arr) => {
                let out = [];
                for (let i = 0, item; item = arr[i]; i++){
                    if (item.isNav)
                        out.push(item);
                    if (item.children && item.children.length)
                        out.push(flat(item.children))
                }
                return out.flat()
            }
            return flat(routes)
        }
    }
}
</script>
