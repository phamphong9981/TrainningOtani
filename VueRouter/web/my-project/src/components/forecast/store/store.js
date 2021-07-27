import { ref, watch, computed } from "@vue/composition-api"
export default function useData() {
    const cityName = ref("")
    const arrayDaily = ref([])
    const loading = ref(null)
    const url = computed(() => {
        return "https://api.openweathermap.org/data/2.5/weather?q=" +
            cityName.value +
            "&appid=604dbe890a4554fab6439b74749da602";
    })

    //function
    function load() {
        loading.value = true
        fetch(url.value).then((response) => response.json()).then((data) => {
            fetch("https://api.openweathermap.org/data/2.5/onecall?lat=" + data.coord.lat + "&lon=" + data.coord.lon + "&exclude=hourly,minutely,alerts&appid=604dbe890a4554fab6439b74749da602").then((response1) => response1.json()).then((data1) => {
                console.log(data1);
                for (const x in data1.daily) {
                    arrayDaily.value.push({
                        time: data1.daily[x].dt,
                        min_temp: parseFloat(data1.daily[x].temp.min - 273.15).toFixed(
                            2
                        ),
                        max_temp: parseFloat(data1.daily[x].temp.max - 273.15).toFixed(
                            2
                        ),
                        weather: data1.daily[x].weather[0].main
                    })
                }
                loading.value = false

            })
        })
    }

    //computed

    //watch
    watch(cityName, () => {
        arrayDaily.value = []
        load()
    })
    return { cityName, url, loading, arrayDaily }
}