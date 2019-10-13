<template>
  <!-- ヘッダナビゲーション -->
  <div id="header">
    <b-navbar toggleable="lg" type="dark" variant="primary">
      <b-navbar-brand to="/">jackkitteの部屋</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
            <b-nav-item to="/profile">プロフィール</b-nav-item>
            <b-nav-item to="/resumecards">経歴一覧</b-nav-item>
          </b-navbar-nav>
          <b-navbar-nav class="ml-auto">
            <b-nav-item-dropdown right v-if="isLoggedIn">
              <template slot="button-content">{{ username }}</template>
              <b-dropdown-item href="/register" @click="clickLogout">ログアウト</b-dropdown-item>
              <b-dropdown-item to="/users">ユーザー一覧</b-dropdown-item>
              <b-dropdown-item to="/register">ユーザー追加</b-dropdown-item>
            </b-nav-item-dropdown>
            <b-nav-item right v-else to="/login">ログイン</b-nav-item>
          </b-navbar-nav>
        </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  computed: {
    username: function () {
      return this.$store.getters['auth/username']
    },
    isLoggedIn: function () {
      return this.$store.getters['auth/isLoggedIn']
    }
  },
  methods: {
    clickLogout: function () {
      this.$store.dispatch('auth/logout')
      this.$store.dispatch('message/setInfoMessage', { message: 'ログアウトしました。' })
      this.$router.replace('/login')
    },
    clickLogin: function () {
      this.$store.dispatch('message/clearMessages')
      this.$router.replace('/login')
    }
  }
}
</script>
