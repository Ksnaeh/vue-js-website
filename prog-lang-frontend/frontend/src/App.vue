<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  <div id="app">
    
    <form @submit.prevent="submitForm">
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
          <td>
            <button class="btn btn-outline-danger btn-sm mx-1" @click="deleteReview(proglang)">Remove</button>
          </td>
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
      proglang: {},
      proglangs: []
    }
  },
  async created(){
    await this.getProglangs()
  },

  //vue functions to link with the html
  methods: {

    //when submit button is pressed
    submitForm(){
      if (this.proglang.id === undefined){
        this.createReview();
      }
      else{
        this.editReview();
      }
    },

    //retrieve function
    async getProglangs(){
      var response = await fetch('http://127.0.0.1:8000/api/review/');
      this.proglangs = await response.json();
    },

    //create function
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
    },

    //update function
    async editReview(){
      await this.getProglangs();

      await fetch(`http://127.0.0.1:8000/api/review/${this.proglang.id}/`, {
        method: 'put',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.proglang)
      });

      await this.getProglangs();
      this.proglang = {}
    },
  
    //delete function
    async deleteReview(proglang){
      await this.getProglangs();

        await fetch(`http://127.0.0.1:8000/api/review/${proglang.id}/`, {
          method: 'delete',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.proglang)
        });

        await this.getProglangs();
        this.proglang = {}
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
