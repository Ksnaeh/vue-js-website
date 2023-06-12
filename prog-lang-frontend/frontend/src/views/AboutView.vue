<template>
  <div class="about">
    <h1>This is an about page</h1>
    <DescriptionPage/>
  </div>
</template>

<script>
// @ is an alias to /src
import DescriptionPage from '@/components/description.vue'

export default {
  name: 'HomeView',
  components: {
    DescriptionPage
  }
}
</script>
