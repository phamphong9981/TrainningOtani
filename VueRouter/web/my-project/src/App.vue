<template>
  <v-app>
    <div id="body">
      <navigation/>
      <div id="my-autocomplete"><my-auto-complete></my-auto-complete></div>
      <transition name="navigation-transion">
        <router-view></router-view>
      </transition>
    </div>
  </v-app>
</template>
<style>
#body {
  background: url(./assets/1.jpg);
  background-size: cover;
  height: 100%;
}
#my-autocomplete {
  width: 70%;
  margin: auto;
}
.navigation-transion-enter, .navigation-transion-leave-to{
  opacity:0
}
.navigation-transion-enter-to, .navigation-transion-leave{
  opacity: 1;
}
.navigation-transion-enter-active, .navigation-transion-leave-active{
  transition: all 1s cubic-bezier(0.165, 0.84, 0.44, 1);
}
</style>
<script>
import Navigation from './components/Navigation.vue';
import MyAutoComplete from "./components/MyAutoComplete.vue";
export default {
  name: "App",
  components: { Navigation,MyAutoComplete },
  setup() {
    
  },
};
</script>