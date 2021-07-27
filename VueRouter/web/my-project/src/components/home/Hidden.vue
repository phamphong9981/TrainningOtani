<template>
  <v-container style="width:85%">
    <table
      id="hidden-background"
      style="
        height: max-content;
        position: relative;
        border-radius: 3vw;
        width: 100%;
      "
    >
      <tr>
        <td style="width: 20%; text-align: center">
          <img
            src="@/assets/wind.png"
            style="width: 10vw; height: 10vw"
            alt=""
          />
        </td>
        <td>
          <p>{{ wind }} m/s</p>
        </td>
      </tr>
      <tr>
        <td style="width: 20%; text-align: center">
          <img
            src="@/assets/cloud.png"
            style="width: 10vw; height: 10vw"
            alt=""
          />
        </td>
        <td>
          <p>{{ cloud }} %</p>
        </td>
      </tr>
      <tr>
        <td style="width: 20%; text-align: center">
          <img
            src="@/assets/location.png"
            style="width: 10vw; height: 10vw"
            alt=""
          />
        </td>
        <td>
          <div>
            <div style="width: 50%; display: inline-block">
              <p>longitude: {{ lon }}</p>
            </div>
            <div style="width: 50%; display: inline-block">
              <p>latitude: {{ lat }}</p>
            </div>
          </div>
        </td>
      </tr>
    </table>
  </v-container>
</template>

<script>
import {  inject } from "@vue/composition-api";
export default {
  setup() {
    let {wind,lon,lat,cloud}=inject("home-store")
    return { wind, lon, lat, cloud };
  },
};
</script>

<style>
#hidden-background::after {
  content: "";
  background: floralwhite;
  position: absolute;
  opacity: 0.2;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  border-radius: 2vw;
}
p {
  color: white;
  text-align: center;
  font-size: 4vw;
  font-family: "Merriweather", serif;
}
</style>