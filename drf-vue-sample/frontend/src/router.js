import Vue from 'vue'
import VueRouter from 'vue-router'
import HomePage from '@/pages/HomePage'
import LoginPage from '@/pages/LoginPage'
import UsersPage from '@/pages/UsersPage'
import UserCreatePage from '@/pages/UserCreatePage'
import store from '@/store'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes: [
    { path: '/', component: HomePage, meta: { requiresAuth: true } },
    { path: '/users',
      component: UsersPage,
      meta: { requiresAuth: true },
      beforeEnter: (to, from, next) => {
        const isSuperUser = store.getters['auth/isSuperUser']
        const isStaff = store.getters['auth/isStaff']
        const isActive = store.getters['auth/isActive']
        console.log('isSuperUser=', isSuperUser)
        console.log('isStaff=', isStaff)
        console.log('isActive=', isActive)

        if (isSuperUser || isStaff) {
          console.log('User is Admin or Staff. So, free to next.')
          next()
        } else if (isActive) {
          console.log('User is Normal. So, redirect to Top Page.')
          forceToLoginPage(to, from, next)
        } else {
          forceToLoginPage(to, from, next)
        }
      }
    },
    { path: '/register', component: UserCreatePage },
    { path: '/login', component: LoginPage },
    { path: '*', redirect: '/'}
  ]
})

router.beforeEach((to, from, next) => {
  const isLoggedIn = store.getters['auth/isLoggedIn']
  const token = localStorage.getItem('access')
  console.log('to.path=', to.path)
  console.log('isLoggedIn=', isLoggedIn)

  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (isLoggedIn) {
      console.log('User is already logged in. So, free to next.')
      next()
    } else {
      if (token != null) {
        console.log('User is not logged in. Trying to reload again.')
        store.dispatch('auth/reload')
          .then(() => {
            console.log('Succeeded to reload. So, free to next.')
            next()
          })
          .catch(() => {
            forceToLoginPage(to, from, next)
          })
      } else {
        forceToLoginPage(to, from, next)
      }
    }
  } else {
    console.log('Go to public page.')
    next()
  }
})

function forceToLoginPage (to, from, next) {
  console.log('Force user to login page.')
  next({
    path: '/login',
    query: { next: to.fullPath}
  })
}

export default router
