import Vue from 'vue'
import Vuex from 'vuex'
import api from '@/services/api'

Vue.use(Vuex)

const authModule = {
  strict: process.env.NODE_ENV !== 'production',
  namespaced: true,
  state: {
    username: '',
    isLoggedIn: false,
    isSuperUser: false,
    isStaff: false,
    isActive: false,
  },
  getters: {
    username: state => state.username,
    isLoggedIn: state => state.isLoggedIn,
    isSuperUser: state => state.isSuperUser,
    isStaff: state => state.isStaff,
    isActive: state => state.isActive,
  },
  mutations: {
    set (state, payload) {
      state.username = payload.user.username
      state.isLoggedIn = true
      state.isSuperUser = payload.user.is_superuser
      state.isStaff = payload.user.is_staff
      state.isActive = payload.user.is_active
    },
    cleare (state) {
      state.username = ''
      state.isLoggedIn = false
      state.isSuperUser = false
      state.isStaff = false
      state.isActive = false
    }
  },
  actions: {
    login (context, payload) {
      return api.post('/auth/jwt/create/', {
        'username': payload.username,
        'password': payload.password
      })
        .then(response => {
          localStorage.setItem('access', response.data.access)
          return context.dispatch('reload')
            .then(user => user)
        })
    },
    logout (context) {
      localStorage.removeItem('access')
      context.commit('clear')
    },
    reload (context) {
      return api.get('/auth/users/me/')
        .then(response => {
          const user = response.data
          console.log(user)
          context.commit('set', { user: user})
          return user
        })
    }
  }
}

const messageModule = {
  strict: process.env.NODE_ENV !== 'production',
  namespaced: true,
  state: {
    error: '',
    warnings: [],
    info: ''
  },
  getters: {
    error: state => state.error,
    warnings: state => state.warnings,
    info: state => state.info
  },
  mutations: {
    set (state, payload) {
      if (payload.error) {
        state.error = payload.error
      }
      if (payload.warnings) {
        state.warnings = payload.warnings
      }
      if (payload.info) {
        state.info = payload.info
      }
    },
    clear (state) {
      state.error = ''
      state.warnings = [],
      state.info = ''
    }
  },
  actions: {
    setErrorMessage (context, payload) {
      context.commit('clear')
      context.commit('set', { 'error': payload.message })
    },
    setWarningMesssages (context, payload) {
      context.commit('clear')
      context.commit('set', { 'warnings': payload.message })
    },
    setInfoMessage (context, payload) {
      context.commit('clear')
      context.commit('set', { 'info': payload.message })
    },
    clearMessages (context) {
      context.commit('clear')
    }
  }
}

const store = new Vuex.Store({
  modules: {
    auth: authModule,
    message: messageModule
  }
})

export default store
