import VueRouter from 'vue-router'
import MyDisplay from "../components/MyDisplay.vue"
import TableFollow from "../components/TableFollow.vue"
const routes = [
    {
        path: "/abc/:city",
        component: MyDisplay,
        props:true
    },
    {
        path: "/table",
        component: TableFollow
    }
]
const router = new VueRouter({
    routes,
    mode: 'history'
})
export default router