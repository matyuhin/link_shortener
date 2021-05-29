import Vue from 'vue'
import Router from 'vue-router'
import store from './store.js'
import Login from './components/Login.vue'
import Edit from './components/Edit.vue'
import Deleted from './components/Deleted.vue'
import Add from './components/Add.vue'
import Register from './components/Register.vue'
import Link from './components/Link.vue'
import Test from './components/Test.vue'
import LinksList from './components/LinksList.vue'

Vue.use(Router)

let router = new Router({
    mode: 'history',
    routes: [
    {
        path: '/',
        name:'home',
        components: {
            viewContent: Link,
            viewSidebar : LinksList
        } ,
        props: { viewContent: true, viewSidebar: false }
    },

    {
        path: '/test',
        name:'test',
        components: {
            viewContent: Test,
        } 
    },

    {
        path: '/add',
        name:'add',
        components: {
            viewContent: Add,
            viewSidebar : LinksList
        } ,
        props: { viewContent: false, viewSidebar: false }
    },

    {
        path: '/deleted',
        name:'del',
        components: {
            viewContent: Deleted,
            viewSidebar : LinksList
        } ,
        props: { viewContent: false, viewSidebar: false }
    },
    
    {
        path: '/link/:id',
        name:'link',
        components: {
            viewSidebar : LinksList,
            viewContent: Link,
        },   
        props: { viewContent: true, viewSidebar: false }
    },

    {
        path: '/login',
        name: 'login',
        components:{
            viewContent: Login
        }, 
    },
    {
        path: '/register',
        name: 'register',
        components:{
            viewContent: Register
        }, 
    },
    {
        path: '/link/edit/:id',
        name: 'edit',
        components:{
            viewSidebar : LinksList,
            viewContent: Edit
        },
        props: { viewContent: true, viewSidebar: false },
        meta: { 
          requiresAuth: true
        }
    },
    ]
  })
  
  router.beforeEach((to, from, next) => {
    if(to.matched.some(record => record.meta.requiresAuth)) {
      if (store.getters.isLoggedIn) {
        next()
        return
      }s
      next('/login') 
    } else {
      next() 
    }
  })
  
export default router