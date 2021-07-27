<template>
  <div style="text-align: center" >
    <div id="date">{{ date }}</div>
    <div><img :src="dir" alt="" style="width: 50%" /></div>
    <div style="width: 100%; display: flex">
      <div id="max_temp">
        <div style="width: 20%;display:flex;align-items:center;justify-content:center">
        <span class="material-icons" style="color: red;font-size:2vw;font-weight:600"> arrow_drop_up </span>
      </div>
      <div style="width: 80%;font-size:1.5vw;margin-right:4%;font-weight:600;color:white">{{ max_temp }}</div>
      </div>
      <div id="min_temp">
        <div style="width: 20%;font-size:1.5vw">
        <span class="material-icons" style="color: green;font-size:2vw;display:flex;align-items:center;justify-content:center;font-weight:600"> arrow_drop_down </span>
      </div>
      <div style="width: 80%;font-size:1.5vw;font-weight:600;color:white">{{ min_temp }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from "@vue/composition-api";
export default {
  props: {
    data: {
      type: Object,
      require: true,
    },
  },
  setup(props) {
    const dir = ref("");
    const date = ref("");
    const max_temp = props.data.max_temp;
    const min_temp = props.data.min_temp;
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
    var d = new Date(props.data.time * 1000);
    date.value =
      d.getDate() + " " + months.value[d.getMonth()] + " " + d.getFullYear();
    if (props.data.weather == "Clouds") {
      dir.value = require("@/assets/Clouds.png");
    } else {
      dir.value = require("@/assets/Rain.png");
    }
    return { dir, date, max_temp, min_temp };
  },
};
</script>

<style scoped>
#max_temp{
  width:45%;
  display: flex;
  position: relative;
  margin-right: 10%;
}
#min_temp{
  width:45%;
  display: flex
}
#date{
  position: relative;
  color: white;
  font-size: 1.5vw;
  font-family: 'Lora', serif;
  margin-bottom: .5vw;
}
#date::before{
  content: "";
  background: red;
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  opacity: 0.2;
}
</style>