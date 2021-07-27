<template>
  <v-container>
    <my-display></my-display>
  </v-container>
</template>

<script>
import { provide, watch } from "@vue/composition-api";
import MyDisplay from "./MyDisplay.vue";
import useData from "./store/store.js";
export default {
  props: {
    cityName: {
      type: String,
      default: "HaNoi",
    },
  },
  components: { MyDisplay },
  setup(props) {
    const store = useData();
    watch(props, (newVal) => {
      store.cityName.value=newVal.cityName
    });
    provide("forecast-store", store);
  },
};
</script>

<style>
</style>