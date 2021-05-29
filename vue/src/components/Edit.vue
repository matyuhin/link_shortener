<template>
  <div class="col-lg-6 mr-auto ml-auto">
    <h1>Редактировать ссылку</h1>
      <p>Оригинальная ссылка: {{link.original}}</p>
      <p>Короткая ссылка: {{link.short}}</p>
      <label for="friendly">Человекопонятная ссылка: </label>
      <div>
          <input id="friendly" name ="friendly" type="text" v-model="friendly" autofocus>
      </div>
      <label for="type_link">Тип ссылки: </label>
      <div>
          <div class="form-check">
            <input type="radio" class="form-check-input" name="type" v-model="type_link" value="1">
            <label class="form-check-label" for="flexRadioDefault1">
                Публичная
            </label>
          </div>
          <div class="form-check">
            <input type="radio" class="form-check-input" name="type" v-model="type_link" value="2">
            <label class="form-check-label" for="flexRadioDefault1">
                Для зарегистрированных пользователей
            </label>
          </div>
          <div class="form-check">
            <input type="radio" class="form-check-input"  name="type" v-model="type_link" value="3">
            <label class="form-check-label" for="flexRadioDefault1">
                Приватная
            </label>
          </div>
      </div>
      <div>
            <button class="btn btn-success" v-on:click="editLink(link.id)">Сохранить</button>
      </div>
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
    }
  },

    methods: {
        getLink(id) {
            const token = localStorage.getItem('token')
            axios(this.endpoint + id, { headers: {"Authorization" : `Bearer ${token}`} })
            .then(response => {
                this.link = response.data
            })
            .catch( error => {
                console.log(error)
            })
        },

        editLink(id) {
            const token = localStorage.getItem('token')
            axios.put(this.endpoint + id, 
                {
                    friendly_link: this.friendly,
                    type_id: this.type_link
                },
                { 
                    headers: {"Authorization" : `Bearer ${token}`}
                }
            )
            .then(() => this.$router.push(`/link/${id}`))
        },
    },
    
    created() {
    this.getLink(this.id);
    },

    watch: {
      '$route'() {
        this.getLink(this.id);
      }
    }
    
}
</script>