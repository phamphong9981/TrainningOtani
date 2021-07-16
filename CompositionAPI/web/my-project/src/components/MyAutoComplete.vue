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
import { ref, inject } from "@vue/composition-api";
export default {
  name: "my-auto-complete",
  setup() {
    const choose = ref("");
    const list = ref([]);
    const display = ref([]);
    const packet = inject("packet");
    const cityName = ref("");
    function handleChange() {
      cityName.value = choose.value.split(",")[0];
      var url =
        "https://api.openweathermap.org/data/2.5/weather?q=" +
        cityName.value +
        "&appid=604dbe890a4554fab6439b74749da602";
      console.log(url);
      console.log(url);
        fetch(url)
          .then((response) => response.json())
          .then((data) => {
            packet.value = data;
            console.log(packet)
          });
      
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