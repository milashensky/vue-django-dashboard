<template lang="html">
    <div class="sidenav sidenav-fixed hide-on-med-and-down grey darken-2 sidenavbar">
        <div class="logo-container">
            <a id="side-logo-container" href="/" class="brand-logo">Brand</a>
        </div>
        <nav-links></nav-links>
    </div>
</template>

<script>
import NavLinks from './NavLinks.vue'
export default {
    components: {
        NavLinks
    }
}
</script>
