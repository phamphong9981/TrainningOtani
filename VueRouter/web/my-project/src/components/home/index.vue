<template>
  <div>
    <div id="display" style="padding-top: 2vw">
      <transition name="display-update-transition"
        ><router-view :key="$route.query.city"></router-view
      ></transition>
    </div>
    <p
      style="
        text-align: center;
        height: 3vw;
        display: flex;
        align-items: center;
        justify-content: center;
      "
    >
      <span
        style="
          color: white;
          cursor: pointer;
          font-size: 1.5vw;
          font-family: 'Zen Loop', cursive;
          text-decoration: none;
        "
        id="detail-link"
        @click="handleHidden"
      >
        View detail
        <span style="position: relative">
          <transition name="icon">
            <span
              key="1"
              class="material-icons icon"
              style="font-size: 2vw"
              v-if="hidden"
            >
              keyboard_arrow_down
            </span>
            <span
              key="2"
              class="material-icons icon"
              style="font-size: 2vw"
              v-else
            >
              keyboard_arrow_up
            </span>
          </transition>
        </span>
      </span>
    </p>
    <transition name="detail-transition">
      <hidden v-if="hidden" />
    </transition>
    <div id="table-follow"><table-follow></table-follow></div>
  </div>
</template>

<script>
import { ref,provide } from "@vue/composition-api";
import TableFollow from "./TableFollow.vue";
import Hidden from "./Hidden.vue";
import useData from "./store/store.js"
export default {
  name: "index",
  components: {  TableFollow, Hidden },
  setup() {
    provide("home-store",useData())
    const hidden = ref(false);
    function handleHidden() {
      hidden.value = !hidden.value;
    }
    function myLog(str) {
      console.log(str);
    }
    return { hidden, handleHidden, myLog };
  },
  destroyed() {
    console.log("abc");
  },
};
</script>

<style scoped>
#table-follow {
  margin-top: 2vw;
}
#detail-link:hover {
  color: dodgerblue !important;
}
#detail-link .icon {
  position: absolute;
  top: 0.2vw;
  left: 0;
  width: 2vw;
  height: 2vw;
}
.icon-enter {
  opacity: 0;
  transform: translateY(5vw);
}
.icon-leave-to {
  opacity: 0;
  transform: translateY(-5vw);
}
.icon-enter-to,
.icon-leave {
  opacity: 1;
}
.icon-enter-active {
  transition: all 1s cubic-bezier(0.165, 0.84, 0.44, 1);
}
.icon-leave-active {
  transition: all 1s cubic-bezier(0.165, 0.84, 0.44, 1);
}
.detail-transition-enter,
.detail-transition-leave-to {
  height: 0;
  opacity: 0;
}
.detail-transition-enter-to,
.detail-transition-leave {
  height: max-content;
  opacity: 1;
}
.detail-transition-enter-active,
.detail-transition-leave-active {
  transition: all 2.5s cubic-bezier(0.19, 1, 0.22, 1);
}
.display-update-transition-enter{
  opacity: 0;
  transform: translateY(10vw);
}
.display-update-transition-leave-to{
  opacity: 0;
  height: 0;
}
.display-update-transition-enter-to, .display-update-transition-leave{
  opacity: 1;
}
.display-update-transition-enter-active{
  transition: all 3s ease;
}
.display-update-transition-leave-active{
  transition: all 1.5s cubic-bezier(0.165, 0.84, 0.44, 1);
}
</style>