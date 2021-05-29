<template>
  <!-- <div class="col-lg-6 mr-auto ml-auto">
    <h1>Добавить ссылку</h1>
      <label for="original">Cсылка: </label>
      <div>
          <input id="original" name ="original" type="text" v-model="original" autofocus>
      </div>
      <label for="friendly">Человекопонятная ссылка: </label>
      <div>
          <input id="friendly" name ="friendly" type="text" v-model="friendly">
      </div>
      <label for="type_link">Тип ссылки: </label>
      <div>
          <input id="type_link" type="text" v-model="type_link" >
      </div>
      <div>
            <button class="btn btn-success" v-on:click="addLink()">Сохранить</button>
      </div>
  </div> -->
  
  <div class="col-lg-6 mr-auto ml-auto">
        <form >
        <h1>Добавить ссылку</h1>
        <div class="form-group">
            <label for="uname">Ссылка:</label>
            <input
            class="form-control"
            required
            id="original"
            type="text" 
            v-model="original"
            name ="original"
            placeholder="Ссылка"
            />
        </div>
        <div class="form-group">
            <label for="uname">Человекопонятная ссылка:</label>
            <input
            class="form-control"
            required
            id="friendly"
            type="text" 
            v-model="friendly"
            name ="friendly"
            placeholder="Человекопонятная ссылка"
            />
        </div>
         <label for="type_link">Тип ссылки: </label>
        <div class="form-check">
            <input type="radio" checked="checked"    class="form-check-input" name="type" v-model="type_link" value="1">
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
          <div class="mt-3">
            <button class="btn btn-primary btn-lg btn-block" v-on:click="addLink()">Сохранить</button>
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
      endpoint_add: 'http://10.170.1.120:5000/add-link',
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

        addLink() {
            const token = localStorage.getItem('token')
            axios.post(this.endpoint_add, 
                {
                    original: this.original,
                    friendly_link: this.friendly,
                    type_id: this.type_link
                },
                { 
                    headers: {"Authorization" : `Bearer ${token}`}
                }
            )
            .then(() => this.$router.push(`/`))
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

<style lang="scss">

</style>