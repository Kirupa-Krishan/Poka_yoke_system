import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '../router'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user_id: localStorage.getItem('user_id') || null,
    user_name:localStorage.getItem('user_name') || null,
    token: localStorage.getItem('token') || null,
    venues:[],
    shows:{},
    loading:true
  },
  getters: {
    user_id(state) {
      return state.user_id
    },
    token(state) {
      return state.token
    },
    is_authenticated(state) {
      return !!state.token
    },
    venues(state){
      return state.venues
    },
    shows(state){
      return state.shows
    },
    is_loading(state){
      return state.loading
    }
  },
  mutations: {
    signup_mutation(state, payload) {
      state.token = payload.data.token
      state.user_id = payload.user_id
    },
    login_mutation(state, payload) {
      state.token = payload.data.token
      state.user_id = payload.user_id
    },
    logout_mutation(state) {
      state.token = null
      state.user_id = null
    },
    getVenues_mutation(state,payload){
      state.venues = payload
    },
    getShows_mutation(state,payload){
      state.shows[payload.venue] = payload.shows
    },
    getSearch_mutation(state,payload){
      state.venues = payload.venue
      state.shows = payload.shows
    },
    clear_data_mutation(state){
      state.venues=[]
      state.shows={}
    },
    is_loading(state,payload){
      state.loading = payload
    }
  },
  actions: {
    async signup_action({ commit }, payload) {
      try {
        const { data } = await axios.post('http://127.0.0.1:5000/auth/signup', payload)
        localStorage.setItem('token', data.token)
        const user_id = JSON.parse(atob(data.token.split('.')[1])).u_id
        const user_name = JSON.parse(atob(data.token.split('.')[1])).u_name
        localStorage.setItem('user_id', user_id)
        localStorage.setItem('user_name',user_name)
        router.push('/home')
        commit('signup_mutation', {data, user_id})
      } catch (error) {
        console.log(error)
      }
    },
    async login_action({ commit }, payload) {
      try {
        const { data } = await axios.post('http://127.0.0.1:5000/auth/login', payload)
        if (data.message === 'Invalid Credentials') {
          alert('Invalid Credentials')
          return
        }
        if(data.admin)
        {
        localStorage.setItem('token', data.token)
        const user_id = JSON.parse(atob(data.token.split('.')[1])).u_id
        const user_name = JSON.parse(atob(data.token.split('.')[1])).u_name
        localStorage.setItem('user_id', user_id)
        localStorage.setItem('user_name', user_name)
        router.push('/admin')
        commit('login_mutation', { data, user_id })
        }
        else{
          localStorage.setItem('token', data.token)
          const user_id = JSON.parse(atob(data.token.split('.')[1])).u_id
          const user_name = JSON.parse(atob(data.token.split('.')[1])).u_name
          localStorage.setItem('user_id', user_id)
          localStorage.setItem('user_name', user_name)
        router.push('/home')
        commit('login_mutation', { data, user_id })
        }
        
      } catch (error) {
        console.log(error)
      }
    },
    async getVenues_action({commit,dispatch}){
          const {data} = await axios.get(`http://127.0.0.1:5000/home/venue/getall`)
          commit('getVenues_mutation',data.venues)
          dispatch('getShows_action',data.venues)
          
      },
      async getShows_action({commit},venues) {
          for(let venue in venues){
            // console.log("Venue Here ",venue)
            try {
              const res = await axios.get(`http://127.0.0.1:5000/home/show/getall/${venue}`)
              commit('getShows_mutation',{'venue':venue,'shows':res.data.shows})
            } catch(err) {
            console.log(err)}
      }
        commit('is_loading',false)
    },
    async getSearch_action({commit},data) {
        try {
          const res = await axios.get(`http://127.0.0.1:5000/home/search?location=${data.location ? data.location:false}&show=${data.show?data.show:false}&rating=${data.rating?data.rating:false}`)
          console.log('query ',data)
          commit('getSearch_mutation',{'venue':res.data.venues,'shows':res.data.shows})
        } catch(err) {
        console.log(err)}
    commit('is_loading',false)
},
    logout_action({ commit }) {
      commit('logout_mutation')
      localStorage.removeItem('token')
      router.push('/')
    },
  },
})
