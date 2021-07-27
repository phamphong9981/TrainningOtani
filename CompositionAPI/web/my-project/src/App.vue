<template>
  <v-app>
    <div id="body">
      <router-link to="/">Home</router-link>
      <router-link to="/table">Content</router-link>
      <div id="my-autocomplete"><my-auto-complete></my-auto-complete></div>
      <div id="display">
        <transition name="my-transition">
          <router-view :key="$route.path"></router-view>
        </transition>
      </div>
      <!-- <div id="table-follow"><table-follow></table-follow></div> -->
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
.my-transition-enter{
  opacity: 0;
  transform: translateY(500px);
}
.my-transition-leave-to{
  opacity: 0;
  height: 0;
}
.my-transition-leave, .my-transition-enter-to{
  opacity: 1;
}
.my-transition-leave-active{
  transition: all 2s cubic-bezier(0.165, 0.84, 0.44, 1);
}
.my-transition-enter-active{
  transition: all 4s ease;
}
</style>
<script scoped>
import { provide,ref } from "@vue/composition-api";
import MyAutoComplete from "./components/MyAutoComplete.vue";
// import TableFollow from "./components/TableFollow.vue";
export default {
  name: "App",
  components: { MyAutoComplete },
  setup() {
    const packet = ref({});
    const dateUpdated=ref("")
    const display=ref([])
    provide("packet", packet);
    provide("dateUpdated",dateUpdated)
    provide("display",display)
    console.log(packet)
    setInterval(function () {
      console.log(packet.value.name)
      if (packet.value.name != undefined) {
        var url =
          "https://api.openweathermap.org/data/2.5/weather?q=" +
          packet.value.name +
          "&appid=604dbe890a4554fab6439b74749da602";
        fetch(url)
          .then((response) => response.json())
          .then((data) => {
            console.log(url);
            packet.value = data;
            var d = new Date();
            dateUpdated.value =
              d.toLocaleTimeString() + "  " + d.toDateString();
          });
      }
    }, 10000);
  },
};
</script>