<template>
  <v-container>
    <div
      style="
        display: flex;
        flex-direction: row-reverse;
        width: 70%;
        margin: auto;
      "
    >
      <v-btn
        dark
        style="height: 4vw; float: right; font-size: 2vw"
        @click="add()"
        >Add to table</v-btn
      >
    </div>
    <div style="height: 50vw; overflow-y: scroll; width: 70%; margin: 5vw auto">
      <table style="width: 100%; color: white; font-size: 2vw">
        <thead style="width: 100%; height: 8vw">
          <th>City</th>
          <th>Temp</th>
          <th>Humidity</th>
          <th>Delete</th>
        </thead>
        <tr v-for="(item, index) in display" :key="index">
          <td>{{ item.name }}</td>
          <td>{{ item.main.temp }}</td>
          <td>{{ item.main.humidity }}</td>
          <td>
            <input
              type="checkbox"
              :value="index"
              v-model="choose"
              style="height: 2vw; width: 2vw"
            />
          </td>
        </tr>
        <tr></tr>
      </table>
    </div>
    <v-container>
      <v-row style="height: 5vw; width: 70%; margin: auto">
        <v-col>
          <v-btn
            large
            v-on:click="removeItem()"
            style="float: right; height: 100%; width: 18vw; font-size: 2vw"
            >Delete</v-btn
          >
        </v-col>
        <v-col>
          <v-btn
            large
            v-on:click="refreshAll()"
            style="float: right; height: 100%; width: 18vw; font-size: 2vw"
            >Refresh All</v-btn
          >
        </v-col>
      </v-row>
    </v-container>
  </v-container>
</template>

<script>
import { inject, ref } from "@vue/composition-api";
export default {
  name: "table-follow",
  setup() {
    const packet = inject("packet");
    const display = ref([]);
    const choose = ref([]);
    const dateUpdated = inject("dateUpdated");
    function add() {
      display.value.push(packet.value);
      console.log(display.value);
    }
    function removeItem() {
      console.log(choose.value);
      choose.value.sort();
      for (let i = choose.value.length - 1; i >= 0; i--) {
        display.value.splice(choose.value[i], 1);
      }
      choose.value = [];
    }
    function refreshAll() {
      var temp = display.value;
      // console.log(temp);
      display.value = [];
      temp.map((item) => {
        var url =
          "https://api.openweathermap.org/data/2.5/weather?q=" +
          item.name +
          "&appid=604dbe890a4554fab6439b74749da602";
        fetch(url)
          .then((response) => response.json())
          .then((data) => {
            console.log(url);
            packet.value = data;
            display.value.push(data);
          });
      });
      var d = new Date();
      dateUpdated.value = d.toLocaleTimeString() + "  " + d.toDateString();
    }
    return {
      packet,
      display,
      add,
      choose,
      removeItem,
      refreshAll,
    };
  },
};
</script>

<style scoped>
th {
  width: 25%;
}
td {
  text-align: center;
}
tr:nth-child(1) {
  height: 100px;
}
tr:nth-last-child() {
  min-height: 0px;
}
</style>