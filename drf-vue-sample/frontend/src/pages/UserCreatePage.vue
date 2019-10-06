<template>
  <div id="user-create-page">
    <GlobalHeader/>
    <GlobalMessage/>

    <main class="container">
      <p class="h5 mb-4">ユーザー登録</p>
      <b-form @submit.prevent="submitRegister">
        <div class="row form-group">
          <label class="col-sm-3 col-form-label">ユーザー名</label>
          <div class="col-sm-8">
            <input type="text" class="form-control" v-model="form.user.username" placeholder="ユーザー名">
          </div>
        </div>
        <div class="row form-group">
          <label class="col-sm-3 col-form-label">メールアドレス</label>
          <div class="col-sm-8">
            <input type="text" class="form-control" v-model="form.user.email" placeholder="メールアドレス">
          </div>
        </div>
        <div class="row form-group">
          <label class="col-sm-3 col-form-label">パスワード</label>
          <div class="col-sm-8">
            <input type="password" class="form-control" v-model="form.user.password" placeholder="パスワード">
          </div>
        </div>
        <div class="row form-group">
          <label class="col-sm-3 col-form-label">パスワード確認用</label>
          <div class="col-sm-8">
            <input type="password" class="form-control" v-model="form.user.repassword" placeholder="パスワード確認用">
          </div>
        </div>
        <div class="row">
          <b-form-checkbox class="col-sm-3" v-model="form.user.isSuperUser">管理者権限</b-form-checkbox>
          <b-form-checkbox class="col-sm-3" v-model="form.user.isStaff">スタッフ権限</b-form-checkbox>
          <b-form-checkbox class="col-sm-3" v-model="form.user.isActive">ログイン権限</b-form-checkbox>
        </div>
        <div class="row text-center mt-5">
          <div class="col-sm-12">
            <b-button type="submit" variant="primary">登録</b-button>
          </div>
        </div>
      </b-form>
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
      form: {
        user: {
          username: '',
          email: '',
          isSuperUser: false,
          isStaff: false,
          isActive: true,
          password: '',
          repassword: '',
        },
      }
    }
  },
  methods: {
    submitRegister: function () {
      api.post('/auth/users/', {
        'username': this.form.user.username,
        'email': this.form.user.email,
        'is_superuser': this.form.user.isSuperUser,
        'is_staff': this.form.user.isStaff,
        'is_active': this.form.user.isActive,
        'password': this.form.user.password,
        're_password': this.form.user.repassword
      })
        .then(response => {
          const message = '登録しました。'
          const user = response.data
          this.$store.dispatch('message/setInfoMessage', { message: message })
          this.form.user.username = user.username
          this.form.user.email = user.email
          this.form.user.isSuperUser = user.is_superuser
          this.form.user.isStaff = user.is_staff
          this.form.user.isActive = use.is_active
        })
    }
  }
}
</script>
