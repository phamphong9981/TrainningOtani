<template>
  <div>
    <button
      @click="nav = !nav"
      id="menu-button"
      style="width: 4vw; height: 4vw"
    >
      <span class="material-icons" style="color: white; font-size: 4vw">
        menu
      </span>
    </button>
    <transition name="menu-transition">
      <div v-if="nav">
        <div class="background" @click="nav=!nav"></div>
        <div id="nav">
          <ul>
            <li>
              <router-link to="/"
                ><b
                  >Home
                  <hr /></b
              ></router-link>
            </li>
            <li style="margin-top: 2vw">
              <router-link to="/forecast"
                ><b
                  >Weather forecast
                  <hr /></b
              ></router-link>
            </li>
          </ul>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
import { ref } from "@vue/composition-api";
export default {
  setup() {
    const nav = ref(false);
    return { nav };
  },
};
</script>

<style scoped>
.background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  background: black;
  opacity: 0.2;
  visibility: visible;
  height: 100%;
  z-index: 1;
}
#menu-button {
  position: fixed;
  top: 1%;
  left: 1%;
  z-index: 10;
}
#nav {
  position: fixed;
  top: 0;
  left: 0;
  width: 30%;
  background: black;
  height: 100%;
  color: white;
  font-size: 2vw;
  z-index: 1;
  opacity: 0.8;
  padding: 6vw 1vw;
}
a {
  text-decoration: none;
}
b {
  color: white;
  font-family: "Fuggles", cursive;
}
hr {
  color: white;
  width: 0;
}
a:hover hr {
  width: 80%;
  transition: 0.5s;
}
ul {
  list-style: none;
  padding: 0;
}
.menu-transition-leave-to{
    opacity: 0;
}
.menu-transition-leave, .menu-transition-enter-to{
    opacity: 1;
}
.menu-transition-enter-active, .menu-transition-leave-active{
    transition: all 1s;
}
</style>