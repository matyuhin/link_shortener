<template>
  
  <div class="col-lg-6 mr-auto ml-auto">
        <form >
        <h1>Добавить ссылку</h1>
          <div class="mt-3">
            <button class="btn btn-primary btn-lg btn-block" v-on:click="testLink()">Сохранить</button>
          </div>
        </form>
    </div>
</template>

<script>


import axios from 'axios';

export default {
  props: ['id'],
  data() {
    return {
      link: null,
      endpoint: 'http://10.170.1.120:5000/links/',
      endpoint_add: 'http://10.170.1.120:5000/test',
    }
  },

    methods: {
        testLink() {
            const token = localStorage.getItem('token')
            axios.post(this.endpoint_add)
            .then(response => {
            this.link = response.data.message
            alert(this.link)
            
            },
            this.$router.push('home')
            )
        },
    },
    
    created() {
    // this.getLink(this.id);
    },

    // watch: {
    //   '$route'() {
    //     this.getLink(this.id);
    //   }
    // }
    
}
</script>

<style lang="scss">

</style>