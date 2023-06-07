<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  <div id="app">
    
    <form @submit.prevent="createReview">
      <div class="form-group row">
        <input type="text" class="form-control col-3 mx-2" placeholder="Name" v-model="proglang.langname">
        <input type="text" class="form-control col-3 mx-2" placeholder="Review" v-model="proglang.review">
        <input type="text" class="form-control col-3 mx-2" placeholder="Rating no." v-model="proglang.rating_no">
        <input type="text" class="form-control col-3 mx-2" placeholder="Username" v-model="proglang.username">
        <button class="btn btn-success">Submit</button>
      </div>
    </form>

    <table class="table">
      <thead>
        <th>Proglang name</th>
        <th>Review</th>
        <th>Rating</th>
        <th>By</th>
      </thead>
      <tbody>
        <tr v-for="proglang in proglangs" :key="proglang.id" @dblclick="$data.proglang = proglang">
          <td>{{ proglang.langname }}</td>
          <td>{{ proglang.review }}</td>
          <td>{{ proglang.rating_no }}</td>
          <td>{{ proglang.username }}</td>
        </tr>
      </tbody>
    </table>
    

  </div>
</template>

<script>
//import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  data(){
    return {
      proglang: {
        'langname': '',
        'review': '',
        'rating_no': '',
        'username': '',
      },
      proglangs: []
    }
  },
  async created(){
    await this.getProglangs()
  },

  methods: {
    async getProglangs(){
      var response = await fetch('http://127.0.0.1:8000/api/review/');
      this.proglangs = await response.json();
    },

    async createReview(){
      await this.getProglangs();

      await fetch("http://127.0.0.1:8000/api/review/", {
        method: 'post',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.proglang)
      });

      await this.getProglangs();
    }
  }
  // components: {
  //   HelloWorld
  // }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
