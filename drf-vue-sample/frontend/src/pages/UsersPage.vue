<template>
  <div id="users-page">
    <GlobalHeader />
    <GlobalMessage />

    <main class="container">
      <p class="h5 mb-4">ホーム</p>
      <div class="columns" v-for="(user, index) in users" :key="index">
        <b-card :header="user.username">
          <b-list-group>
            <b-list-group-item>{{ user.url }}</b-list-group-item>
            <b-list-group-item>{{ user.email }}</b-list-group-item>
            <b-list-group-item>{{ user.is_staff }}</b-list-group-item>
          </b-list-group>
        </b-card>
      </div>
    </main>
  </div>
</template>

<script>
import api from '@/services/api'
import GlobalHeader from '@/components/GlobalHeader.vue'
import GlobalMessage from '@/components/GlobalMessage.vue'

export default {
  components: {
    GlobalHeader,
    GlobalMessage
  },
  data () {
    return {
      users: []
    }
  },
  created () {
    api.get('/users/')
      .then(response => {
        this.users = response.data
      })
  }
}
</script>
