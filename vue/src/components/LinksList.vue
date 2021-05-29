
<template>
    <div>
        <ul class="list-group">
          <router-link
              v-for="link in links" :key="link.id"
              active-class="active"
              class="list-group-item lst"
              :to="{ name: 'link', params: { id: link.id } }">
            <!-- <li class="list-group-item" active-class="active"><p>{{link.original}}</p></li> -->
            <p>{{link.original}}</p>
          </router-link>
        </ul>
    </div>
</template>


<script>
  import axios from 'axios'
  export default {
    computed : {
      isLoggedIn : function(){ return this.$store.getters.isLoggedIn}
    },

    data () {
      return {
        links: null,
        test:"test",
        endpoint: 'http://10.170.1.120:5000/links',
      }
    },
    created() {
      this.getAllLinks();
    },
    methods: {
      getAllLinks() {
        const token = localStorage.getItem('token')
        axios.get(this.endpoint, { headers: {"Authorization" : `Bearer ${token}`} })
          .then(response => {
            this.links = response.data;
          })
          .catch(error => {
            console.log('-----error-------');
            console.log(error);
          })
      },
      
    },

    watch: {
      '$route'() {
        this.getAllLinks();
      }
    }

    // created: function () {
    //   this.$http.interceptors.response.use(undefined, function (err) {
    //     return new Promise(function (resolve, reject) {
    //       if (err.status === 401 && err.config && !err.config.__isRetryRequest) {
    //         this.$store.dispatch(logout)
    //       }
    //       throw err;
    //     });
    //   });
    // }
  }
  
</script>

<style lang="scss">
  .lst {
      // border-right: none;
      text-decoration: none;
  }
</style>

