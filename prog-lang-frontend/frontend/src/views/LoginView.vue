<template>
    <div>
      <LoginPage/>
    </div>
  </template>
  
  <script>
  // @ is an alias to /src
  import LoginPage from '@/components/loginComponent.vue'
  
  export default {
    name: 'HomeView',
    components: {
        LoginPage
    }
  }
  </script>