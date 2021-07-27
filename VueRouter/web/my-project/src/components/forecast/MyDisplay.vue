<template>
  <div>
    <div id="cityName">{{ cityName }}</div>
    <!-- <h1>{{arrayDaily}}</h1> -->
    
    <div style="display: flex;width:100%;flex-wrap:wrap" id="table">
      <div v-for="item in arrayDaily" :key="item.id" style="width:25%;padding: 2vw; box-sizing: border-box;border:0.1vw solid black">
        <my-item :data="item" />
      </div>
    </div>
    <loader object="#ff9633" color1="#ffffff" color2="#17fd3d" size="5" speed="2" bg="#343a40" objectbg="#999793" opacity="80" name="circular" v-if="loading"></loader>
  </div>
</template>

<script>
import { inject } from "@vue/composition-api";
import MyItem from "./MyItem.vue";
export default {
  components: { MyItem },
  setup() {
    const { cityName, loading, arrayDaily } = inject("forecast-store");

    return { cityName, loading, arrayDaily };
  },
};
</script>

<style scoped>
#cityName {
  color: white;
  font-size: 8vw;
  font-family: "Zen Loop", cursive;
  text-align: center;
  
}
#table{
  position: relative;
  background: rgba(41, 41, 41, 0.7);
  border-radius: 3vw;
  overflow: hidden;
  box-shadow: 1vw black;
  margin-top: 2vw;
}
</style>