import { computed, ref, watch } from "@vue/composition-api";
export default function useData() {
    //declare
    const cityName = ref("HaNoi")
    const dateUpdated = ref("");
    const packet = ref(null)
    const show = ref(true)
    const displayDate = ref("")
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
    const url = computed(() => {
        return "https://api.openweathermap.org/data/2.5/weather?q=" +
            cityName.value +
            "&appid=604dbe890a4554fab6439b74749da602";
    })

    //function
    async function load() {
        console.log(url.value);
        await fetch(url.value)
            .then((response) => response.json()).then((data) => {
                packet.value = data
            })
        var d = new Date();
        day.value = days.value[d.getDay()];
        month.value = months.value[d.getMonth()];
        year.value = d.getFullYear();
        date.value = d.getDate();
        displayDate.value =
            day.value + ", " + date.value + " " + month.value + " " + year.value;
        dateUpdated.value = d.toLocaleTimeString() + "  " + d.toDateString();
    }
    load()
    console.log("abc");
    function reload() {
        load()
    }

    //computed 
    const humidity = computed(() => {
        return  packet.value?.main.humidity;
    })

    const wind = computed(() => {
        return packet.value?.wind.speed;
    });
    const cloud = computed(() => {
        return packet.value?.clouds.all;
    });
    const lat = computed(() => {
        return packet.value?  parseFloat(packet.value.coord.lat).toFixed(2):null;
    });
    const lon = computed(() => {
        return packet.value? parseFloat(packet.value.coord.lon).toFixed(2):null;
    });
    const temperature = computed(() => {
        return packet.value? parseFloat(packet.value.main.temp - 273.15).toFixed(
            2
        ):null;
    })


    //watch
    watch(cityName, () => {
        load()
    })
    return { packet, dateUpdated, show, temperature, cityName, load, displayDate, humidity, wind, lon, lat, cloud, reload }
}