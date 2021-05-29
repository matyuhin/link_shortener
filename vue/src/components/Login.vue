<template>
    <div class="col-lg-6 mr-auto ml-auto">
        <form @submit.prevent="login">
        <h1>Вход</h1>
        <div class="form-group">
            <label for="uname">Адрес электронной почты:</label>
            <input
            class="form-control"
            required
            v-model="email"
            type="email"
            placeholder="Email"
            />
        </div>
        <div class="form-group">
            <label for="pwd">Пароль:</label>
            <input
            required
            class="form-control"
            v-model="password"
            type="password"
            placeholder="Password"
            />
        </div>
        <button type="submit" class="btn btn-primary btn-lg btn-block">Войти</button>
        </form>
        <!-- <h3>{{data.message}}</h3> -->
    </div>
</template>

<script>
export default {
  data() {
    return {
      email: "",
      password: "",
    };
  },

  methods: {
    login: function () {
      let email = this.email;
      let password = this.password;
      this.$store
        .dispatch("login", { email, password })
        .then(() => this.$router.push("/"))
        // .then(response => {
        //     this.data = response.data
        //     alert("sdsadsd")
        //     },
        //     // this.$router.push('/')
        //     )
        .catch(
            (err) => console.log(err),
            // alert("sdsadsd"),
            (response) => {
            this.data = response.data
            // alert("sdsadsd")
            },
            );
    },
  },
};
</script>