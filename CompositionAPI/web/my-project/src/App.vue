<template>
  <v-app>
    <div id="body">
      <div id="my-autocomplete"><my-auto-complete></my-auto-complete></div>
      <div id="display"><my-display></my-display></div>
      <div id="table-follow"><table-follow></table-follow></div>
    </div>
  </v-app>
</template>
<style>
#body {
  background: url(./assets/1.jpg);
  background-size: cover;
  height: 100%;
}
#my-autocomplete{
  width: 70%;
  margin: auto;
}
</style>
<script scoped>
import { provide,ref } from "@vue/composition-api";
import MyAutoComplete from "./components/MyAutoComplete.vue";
import MyDisplay from "./components/MyDisplay.vue";
import TableFollow from "./components/TableFollow.vue";
export default {
  name: "App",
  components: { MyAutoComplete, MyDisplay ,TableFollow},
  setup() {
    const packet = ref({});
    const dateUpdated=ref("")
    provide("packet", packet);
    provide("dateUpdated",dateUpdated)
    console.log(packet)
  },
};
</script>