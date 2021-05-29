<template>
  <div class="col-lg-6 mr-auto ml-auto">
    <form @submit.prevent="register">
        <h1>Регистрация</h1>
        <div class="form-group">
          <label for="email">Ваше имя:</label>
          <input
            required
            class="form-control"
            name="name"
            v-model="name"
            type="text"
            placeholder="Ваше имя"
          />
        </div>
        <div class="form-group">
          <label for="email">Адрес электронной почты:</label>
          <input
            required
            class="form-control"
            name="email"
            v-model="email"
            type="email"
            placeholder="Email"
          />
        </div>
        <div class="form-group">
          <label for="password">Пароль:</label>
          <input
            required
            name="password"
            class="form-control"
            v-model="password"
            type="password"
            placeholder="Пароль"
          />
        </div>
        <button type="submit" class="btn btn-primary btn-lg btn-block">Зарегистрироваться</button>
      </form>
      <!-- ----------------------------------------------------------------------------------- -->
    <!-- <form @submit.prevent="register">
      <label for="name">Name</label>
      <div>
          <input id="name" type="text" v-model="name" required autofocus>
      </div>
      <label for="email" >E-Mail Address</label>
      <div>
          <input id="email" type="email" v-model="email" required>
      </div>
      <label for="password">Password</label>
      <div>
          <input id="password" type="password" v-model="password" required>
      </div>
      <label for="password-confirm">Confirm Password</label>
      <div>
          <input id="password-confirm" type="password" v-model="password_confirmation" required>
      </div>
      <div>
          <button type="submit">Register</button>
      </div>
    </form> -->
  </div>
</template>

<script>
  export default {
    data(){
      return {
        name : "",
        email : "",
        password : "",
        password_confirmation : "",
      }
    },
    methods: {
      register: function () {
        let data = {
          name: this.name,
          email: this.email,
          password: this.password,
        }
        this.$store.dispatch('register', data)
       .then(() => this.$router.push('/'))
       .catch(err => console.log(err))
      }
    }

  }
</script>