import VueRouter from 'vue-router'
import home from "../components/home"
import forecast from "../components/forecast"
import MyDisplay from "../components/home/MyDisplay.vue"
const routes = [
    {
        path: "/",
        component: home,
        children: [{
            path: "",
            component: MyDisplay,
            props: route => ({ city: route.query.city })
        }]
    },
    {
        path: "/forecast",
        component: forecast,
        props:route=>({cityName:route.query.city})
    }
]
const router = new VueRouter({
    routes,
    mode: 'history'
})
router.beforeEach((to,from,next)=>{
    console.log("trans");
    // if(!to.query.city){
    //     next({path:to.path, query:{city:"HaNoi"}})
    // }
    next()
})
export default router