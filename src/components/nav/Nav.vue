<template lang="html">
    <div class="navbar-fixed">
        <nav class="grey darken-2 topnav" role="navigation">
            <div class="nav-wrapper">
                <a id="logo-container" href="/" class="brand-logo">Brand</a>
                <ul class="right hide-on-med-and-down">
                    <li>
                        <a href="/logout">Sign out</a>
                    </li>
                </ul>

                <nav-links id="nav-mobile" class="sidenav">
                    <li><a href="/logout">Sign out</a></li>
                </nav-links>
                <a href="#" data-target="nav-mobile" class="sidenav-trigger">
                    <i class="material-icons">menu</i>
                </a>
            </div>
        </nav>
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

<style lang="css">
</style>
