<template>
  <v-container>
    <div id="city-name">{{ cityName }}</div>
    <div id="date-time">{{ displayDate }}</div>
    <div id="data">
      <div id="temperature">{{ temperature }}&#8451;</div>
      <div id="humidity">{{ humidity }}%</div>
    </div>
    <div id="time-updated">Updated: {{ dateUpdated }}</div>
    <v-btn dark style="height: 4vw; float: right; font-size: 2vw" @click="add()"
      >Add to table</v-btn
    >
  </v-container>
</template>

<script scoped>
import { ref, inject, watch } from "@vue/composition-api";
import router from "../router/router.js";
export default {
  name: "my-display",
  props: {
    city: {
      type: String,
      default: ""
    },
  },
  setup(props) {
    const packet = inject("packet");
    const cityName = ref("");
    const humidity = ref("");
    const temperature = ref("");
    const dateUpdated = inject("dateUpdated");
    const days = ref([
      "Sunday",
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
    ]);
    const months = ref([
      "January",
      "February",
      "March",
      "April",
      "May",
      "June",
      "July",
      "August",
      "September",
      "October",
      "November",
      "December",
    ]);
    const day = ref("");
    const month = ref("");
    const year = ref("");
    const date = ref("");
    const displayDate = ref("");
    const display = inject("display");
    
    
    console.log(router);
    cityName.value=props.city
    if (cityName.value != "") {
      var url =
        "https://api.openweathermap.org/data/2.5/weather?q=" +
         cityName.value+
        "&appid=604dbe890a4554fab6439b74749da602";
      console.log(url);
      console.log(url);
      fetch(url)
        .then((response) => response.json())
        .then((data) => {
          packet.value = data;
          console.log(packet);
        });
    }
    function add() {
      display.value.push(packet.value);
      console.log(display.value);
    }
    watch(()=>props.city,(newValue)=>{
      cityName.value=newValue
    })
    watch(packet, (newValue) => {
      cityName.value = newValue.name;
      var d = new Date();
      day.value = days.value[d.getDay()];
      month.value = months.value[d.getMonth()];
      year.value = d.getFullYear();
      date.value = d.getDate();
      displayDate.value =
        day.value + ", " + date.value + " " + month.value + " " + year.value;
      temperature.value = parseFloat(newValue.main.temp - 273.15).toFixed(2);
      humidity.value = newValue.main.humidity;
      console.log(newValue.name);
      dateUpdated.value = d.toLocaleTimeString() + "  " + d.toDateString();
    });

    return {
      packet,
      cityName,
      temperature,
      displayDate,
      dateUpdated,
      humidity,
      add,
    };
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
  height: 10vw;
}
#data {
  margin: 2vw auto;
  color: white;
  font-size: 6vw;
  width: 60vw;
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
  font-weight: 400;
}
</style>>