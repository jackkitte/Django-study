<template>
  <div id="user-create-page">
    <GlobalHeader/>
    <GlobalMessage/>

    <b-container class="container" id="user-create-container">
      <p class="h5 mb-4">ユーザー登録</p>
      <b-form @submit.prevent="submitRegister">
        <b-form-group label="ユーザー名" label-for="input-user">
          <b-form-input id="iput-user" type="text" v-model="form.user.username" placeholder="ユーザー名">
          </b-form-input>
        </b-form-group>
        <b-form-group label="メールアドレス" label-for="input-email">
          <b-form-input id="iput-email" type="email" v-model="form.user.email" placeholder="メールアドレス">
          </b-form-input>
        </b-form-group>
        <b-form-group label="パスワード" label-for="input-password">
          <b-form-input id="iput-password" type="password" v-model="form.user.password" placeholder="パスワード">
          </b-form-input>
        </b-form-group>
        <b-form-group label="パスワード確認用" label-for="input-repassword">
          <b-form-input id="iput-repassword" type="password" v-model="form.user.repassword" placeholder="パスワード確認用">
          </b-form-input>
        </b-form-group>
        <b-form-row>
          <b-form-checkbox class="pr-2" v-model="form.user.isSuperUser">管理者権限</b-form-checkbox>
          <b-form-checkbox class="pr-2" v-model="form.user.isStaff">スタッフ権限</b-form-checkbox>
          <b-form-checkbox class="pr-2" v-model="form.user.isActive">ログイン権限</b-form-checkbox>
        </b-form-row>
        <div class="row text-center mt-5">
          <div class="col-sm-12">
            <b-button type="submit" variant="primary">登録</b-button>
          </div>
        </div>
      </b-form>
    </b-container>
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
          this.form.user.isActive = user.is_active
        })
    }
  }
}
</script>

<style scoped>
</style>
