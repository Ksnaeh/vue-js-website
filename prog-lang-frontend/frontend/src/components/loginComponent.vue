<template>
    <div id="app" class="hello">
        <p> {{ msg }} </p>

    <form @submit.prevent="loginForm">
      <div class="form-group row">
        <input type="text" class="form-control col-3" placeholder="Username" v-model="uname">
        <input type="text" class="form-control col-3 mt-2" placeholder="Password" v-model="pword">
        
        <button class="btn btn-success mt-5">Login</button>
        <button class="btn btn-success mt-1">Sign up</button>
      </div>
    </form>

    </div>
</template>

<script>

    export default {
        name: 'LoginPage',
        data () {
            return {
                user: {},
                users: [],
                msg: 'login page here'
            }
        },
        async created(){
            await this.getUsers()
        },
        methods: {

            async getUsers(){

                //retrieve users
                var response = await fetch('http://127.0.0.1:8000/api/user/');
                this.users = await response.json();

                console.log(this.users)
            },

            loginForm(){
                if (this.uname === undefined || this.uname === "" || this.pword === undefined || this.pword === ""){
                    window.alert("PLEASE ENTER A USERNAME/PASSWORD")
                }
                else{
                    console.log("username: " + this.uname);
                    console.log("password: " + this.pword);

                    this.users.forEach(user => {
                        if (this.uname == user.name && this.pword == user.password){
                            window.alert("success!")
                            
                            //add sessionstorage + navigation here

                            
                            return
                        }
                        
                    });



                }
            }        

        }
    }
        

</script>

<style scoped>
    h1, h2 {
        font-weight: normal;
    }

    ul {
        list-style-type: none;
        padding: 0;
    }

    li {
        display: inline-block;
        margin: 0 10px;
    }

    a {
        color: #42b983;
    }
</style>