
<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container-fluid">
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarTogglerDemo03"
          aria-controls="navbarTogglerDemo03"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <router-link v-if="isLoggedIn" to="/"><a class="navbar-brand"><img width="200px" src="./assets/logo.png" alt=""></a></router-link> 
        <router-link v-else to="/login"><a class="navbar-brand"><img width="200px" src="./assets/logo.png" alt=""></a></router-link> 
        <div class="collapse navbar-collapse" id="navbarTogglerDemo03">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item">

            </li>
          </ul>
          <ul v-if="isLoggedIn" class="navbar-nav">
            <router-link :to="{ name: 'add' }">
              <button class="btn btn-outline-light">
                Создать ссылку
              </button></router-link
            >
          </ul>
          <ul v-if="isLoggedIn" class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link" @click="logout">Выйти</a>
            </li>
          </ul>
          <ul v-else class="navbar-nav">
            <li class="nav-item">
              <router-link to="/login"
                ><a class="nav-link" aria-current="page">Войти</a></router-link
              >
            </li>
            <li class="nav-item">
              <router-link to="/register"
                ><a class="nav-link" aria-current="page"
                  >Зарегистрироваться</a
                ></router-link
              >
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <div class="container-fluide">
      <div class="row">
        <div class="col-lg-4 pt-5 sidebar">
          <router-view class="view two" name="viewSidebar"></router-view>
        </div>
        <div class="col-lg-8 pt-5 contents">
          <router-view class="view three" name="viewContent"></router-view>
        </div>
      </div>
    </div>
    

  </div>
</template>


<script>
import axios from "axios";
import LinksList from "./components/LinksList.vue";
export default {
  components: {
    LinksList,
  },
  computed: {
    isLoggedIn: function () {
      return this.$store.getters.isLoggedIn;
    },
  },

  methods: {
    logout: function () {
      this.$store.dispatch("logout").then(() => {
        this.$router.push("/login");
      });
    },
  },
  created: function () {
    this.$http.interceptors.response.use(undefined, function (err) {
      return new Promise(function (resolve, reject) {
        if (err.status === 401 && err.config && !err.config.__isRetryRequest) {
          this.$store.dispatch("logout")
        }
        throw err;
      });
    });
  }
};
</script>

<style lang="scss">
.sidebar{
  background-color:#f5f6f7;
  min-height: 100vh;
  padding-right: 0;
}
</style>