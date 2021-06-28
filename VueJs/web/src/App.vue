<template>
  <v-app>
    <v-container>
      <v-row >
        <v-col
          class="d-flex"
          cols="6"
          sm="6"
        >
          <v-select
            v-model="select"
            :items="listdetail"
            item-text="Name"
            item-value="Content"
            label="Solo field"
            solo
            return-object
          >
          </v-select>
        </v-col>
        <v-col class="d-flex"
          cols="6"
          sm="6">
          <v-col cols="3" offset="2">
            <v-btn block v-on:click="addItem()">
              Add
            </v-btn>
          </v-col>
        </v-col>
      </v-row>
    </v-container>
    <table style="min-height:500px">
      <tr>
        <th>City</th>
        <th>Temp</th>
        <th>Cloud</th>
        <th>Humidity</th>
        <th>Delete</th>
      </tr>
      <tr v-for="(item,index) in display" :key="index">
        <td>{{item.Name}}</td>
        <td>{{item.Content.Temp}}</td>
        <td>{{item.Content.Cloud}}</td>
        <td>{{item.Content.Humidity}}</td>
        <td><input type="checkbox" :value="index" v-model="choose"></td>
      </tr>
      <tr></tr>
    </table>
    <v-container>
      <v-row>
        <v-col col="1" offset="8">
          <v-btn large v-on:click="removeItem()">Delete</v-btn>
        </v-col>
        <v-col col="2" offset="0">
          <v-btn large v-on:click="refreshAll()">Refresh All</v-btn>
        </v-col>
      </v-row>
    </v-container>

  </v-app>  
</template>
<style>
td{
  text-align: center;
}
tr:nth-child(1){
  height: 100px;
}
tr:nth-last-child(){
  min-height: 0px;
}
</style>
<script>

export default {
  name: 'App',

  components: {
    
  },

  data: () => ({
    count: 0,
    choose: [],
    display:[],
    select: { Name: 'Ha Noi',Content:{Temp:"27",Cloud:"10m/s", Humidity:"80%"},id:0},
    listdetail: [
      {
        Name: "Ha Noi",
        Content:{
          Temp:"27",
          Cloud:"10m/s",
          Humidity:"80%"
        }
      },
      {
        Name:"Paris",
        Content:{
          Temp:"28",
          Cloud:"10m/s",
          Humidity:"80%"
        }
      },
      {
        Name:'London',
        Content:{
          Temp:"29",
          Cloud:"10m/s",
          Humidity:"80%"
        }
      },
      {
        Name:'Tokyo',
        Content:{
          Temp:"30",
          Cloud:"10m/s",
          Humidity:"80%"
        }
      },
      {
        Name:'Seoul',
        Content:{
          Temp:"31",
          Cloud:"10m/s",
          Humidity:"80%"
        }
      }
    ]
  }),
  methods:{
    addItem: function(){
      this.count++
      this.select.id=this.count
      this.display.push(this.select)
      console.log(this.display)
    },
    removeItem(){
      console.log(this.choose)
      this.choose.sort()
      for(let i=this.choose.length-1;i>=0;i--){
        this.display.splice(this.choose[i],1)
      }
      this.choose=[]
    },
    refreshAll(){
      this.display=[]
      this.choose=[]
    }
  }
};
</script>
