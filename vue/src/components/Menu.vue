<template>
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
        <router-link to="/"><a class="navbar-brand"><img width="200px" src="./assets/logo.png" alt=""></a></router-link> 
        <div class="collapse navbar-collapse" id="navbarTogglerDemo03">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item">

            </li>
          </ul>
          <ul class="navbar-nav">
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
</template>
<script>
import { defineComponent } from '@vue/composition-api'

export default defineComponent({
    setup() {
        
    },
})
</script>
