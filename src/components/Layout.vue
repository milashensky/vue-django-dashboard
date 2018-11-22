<template>
    <div class="main grey lighten-5">
        <top-nav/>
        <side-nav/>
        <div class="content-container">
          <div class="container">
              <router-view></router-view>
          </div>
        </div>
        <vue-footer/>
    </div>
</template>

<script>
import TopNav from "./nav/Nav.vue";
import SideNav from "./nav/SideNav.vue";
import VueFooter from "./nav/Footer.vue";

export default {
    components: {
        TopNav,
        SideNav,
        VueFooter,
    }
};
</script>
<style media="screen">
    .main {
        min-height: calc(100vh - 210px);
    }
</style>
