<template>
  <v-container style="padding-top: 0">
    <div id="city-name">{{ cityName }}</div>
    <div id="date-time">{{ displayDate }}</div>
    <div id="data">
      <div id="temperature">{{ temperature }}&#8451;</div>
      <div id="humidity">{{ humidity }}%</div>
    </div>
    <div id="time-updated">Updated: {{ dateUpdated }}</div>
  </v-container>
</template>

<script>
import { inject, ref } from "@vue/composition-api";
export default {
  name: "my-display",
  props: {
    city: {
      type: String,
      default: "HaNoi",
    },
  },
  setup(props) {
    const {
      dateUpdated,
      temperature,
      cityName,
      displayDate,
      humidity,
      reload,
    } = inject("home-store");

    const myInterval = ref(null);
    cityName.value = props.city;
    
    myInterval.value = setInterval(function () {
      reload();
    }, 10000);


    return {
      cityName,
      temperature,
      displayDate,
      dateUpdated,
      humidity,
      myInterval,
    };
  },
  destroyed() {
    clearInterval(this.myInterval);
    console.log("destroyed");
  },
};
</script>

<style scoped>
#city-name {
  width: 70%;
  margin: auto;
  font-size: 6vw;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
}
#data {
  margin: 2vw auto;
  color: white;
  font-size: 5.5vw;
  width: 70%;
  font-family: Georgia, "Times New Roman", Times, serif;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 11vw;
}
#temperature {
  width: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  height: 100%;
}
#humidity {
  width: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  height: 100%;
}
#temperature::after {
  content: "";
  width: 100%;
  height: 100%;
  background-color: white;
  position: absolute;
  top: 0;
  left: 0;
  opacity: 0.4;
  border-top-left-radius: 10%;
  border-bottom-left-radius: 10%;
}
#humidity::after {
  content: "";
  width: 100%;
  height: 100%;
  background-color: black;
  position: absolute;
  top: 0;
  left: 0;
  opacity: 0.4;
  border-top-right-radius: 10%;
  border-bottom-right-radius: 10%;
}
#date-time {
  text-align: center;
  color: white;
  font-size: 1vw;
}
#time-updated {
  color: white;
  font-size: 1.5vw;
  text-align: center;
  font-weight: 600;
}
</style>>