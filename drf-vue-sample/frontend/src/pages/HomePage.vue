<template>
  <div id="home-page">
    <GlobalHeader/>
    <GlobalMessage/>

    <div class="py-4">
      <b-jumbotron header="jackkitteの部屋へようこそ！" bg-variant="info" text-variant="white">
        <p>Vue.jsとDjango + django-rest-frameworkとBootstrapVueでプロフィールサイトを作ってみました！！</p>
        <b-button variant="primary" to="/profile">プロフィール</b-button>
      </b-jumbotron>
      <b-carousel
        id="carousel-1"
        v-model="slide"
        :interval="4000"
        controls
        indicators
        background="#ababab"
        img-width="1024"
        img-height="480"
        style="text-shadow: 1px 1px 2px #333;"
        @sliding-start="onSlideStart"
        @sliding-end="onSlideEnd"
      >
        <b-carousel-slide
          caption="Hello!, I'm Pythonista."
          text="We are developing a LINE disaster prevention chatbot in Python!"
          img-src="https://picsum.photos/1024/480/?image=52"
        ></b-carousel-slide>
        <b-carousel-slide
          caption="I love Python3!"
          text="Recently I have been developing with Vue.js for studying the front end."
          img-src="https://picsum.photos/1024/480/?image=54">
        </b-carousel-slide>
        <b-carousel-slide
          caption="I love AWS too!"
          text="We are also developing on AWS!"
          img-src="https://picsum.photos/1024/480/?image=58"
        ></b-carousel-slide>
        <b-carousel-slide
          caption="I love Anime!"
          img-src="https://picsum.photos/1024/480/?image=10"
        ></b-carousel-slide>
        <b-carousel-slide img-src="https://picsum.photos/1024/480/?image=55">
          <h1>Thank you for being here!</h1>
        </b-carousel-slide>
      </b-carousel>

    </div>
  </div>
</template>

<script>
import GlobalHeader from '@/components/GlobalHeader.vue'
import GlobalMessage from '@/components/GlobalMessage.vue'

export default {
  components: {
    GlobalHeader,
    GlobalMessage
  },
  data() {
    return {
      slide: 0,
      sliding: null
    }
  },
  methods: {
    onSlideStart(slide) {
      this.sliding = true
    },
    onSlideEnd(slide) {
      this.sliding = false
    }
  }
}
</script>
