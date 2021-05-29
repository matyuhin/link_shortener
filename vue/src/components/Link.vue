<template lang="html">
  <div class="col-lg-6 mr-auto ml-auto" v-if="link">
    <p>Оригинальная ссылка: <a :href="link.original">{{ link.original }}</a></p>
    <p>Короткая ссылка: <a :href="link.short">{{ link.short }}</a></p>
    <p v-if="link.friendly">Человекопонятная ссылка: <a :href="link.friendly">{{ link.friendly }}</a></p>
    <p>Тип: {{ link.type_id }}</p>
    <p>Количество переходов: {{ link.counter }}</p>

    <router-link :to="{ name: 'edit', params: { id: link.id } }">
          <button class="btn btn-success"v-on:click="editLink(link.id)">Редактировать</button></router-link>
          <button class="btn btn-danger" v-on:click="deleteLink(link.id)">Удалить</button>
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

    deleteLink(id) {
      const token = localStorage.getItem('token')
            axios.delete(this.endpoint + id, 
                { 
                    headers: {"Authorization" : `Bearer ${token}`}
                }
            )
            // .then(() => this.$router.push(`/`))
            .then(() => this.$router.push({ name: 'del'}))

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
