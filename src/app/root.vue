<template>
	<div class="main grey lighten-5" id="app">
		<top-nav/>
		<side-nav/>
		<div class="content-container">
			<div class="container">
				<p>Here</p>
			</div>
		</div>
		<router-view></router-view>
		<vue-footer/>
	</div>
</template>

<script>
import VueFooter from './components/nav/footer.vue';
import TopNav from './components/nav/sidenav.vue';
import SideNav from './components/nav/nav.vue';

export default {
	components: {
		VueFooter,
		TopNav,
		SideNav,
	}
}
</script>
