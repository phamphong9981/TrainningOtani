<template>
  <div id="auto-com">
    <v-container>
      <div style="height: 6vw;">
        <v-autocomplete
          filled
          background-color="#C093B0"
          style="border-radius: 0px 20px 0px 20px; padding-left: 10px"
          :items="display"
          v-model="choose"
          @change="handleChange"
          hide-details=true
        >
        </v-autocomplete>
      </div>
    </v-container>
  </div>
</template>

<script scoped>
import { ref } from "@vue/composition-api";
import router from "../router/router.js"
export default {
  name: "my-auto-complete",
  setup() {
    const choose = ref("");
    const list = ref([]);
    const display = ref([]);
    const cityName = ref("");
    function handleChange() {
      cityName.value = choose.value.split(",")[0];
      router.push({query:{city:cityName.value}})
    }

    fetch("https://countriesnow.space/api/v0.1/countries/capital")
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        data.data = data.data.filter(
          (value) => value.capital != "" && value.name != ""
        );
        data.data.forEach((element) => {
          list.value.push(element);
        });
        display.value = list.value.map(
          (value) => value.capital + ", " + value.name
        );
        console.log(display.value);
      });
    return { list, display, choose, handleChange };
  },
};
</script>

<style scoped>
#app {
  background: transparent;
  height: max-content;
}
</style>