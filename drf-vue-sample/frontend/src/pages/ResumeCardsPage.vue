<template>
  <div id="resume-cards-page">
    <GlobalHeader/>
    <GlobalMessage/>

    <main class="container mt-4">
      <b-row>
        <b-col md=12 class="text-right mb-4">
          <div class="d-flex justify-content-between">
            <h3>経　歴　一　覧</h3>
            <router-link to="/resumecards/add" class="btn btn-info">Add Resume</router-link>
          </div>
        </b-col>
        <template v-for="resume in resumes">
          <div :key="resume.id" class="col-lg-3 col-md-4 col-sm-6 mb-4">
            <ResumeCard :onDelete="deleteResume" :resume="resume"/>
          </div>
        </template>
      </b-row>
    </main>
  </div>
</template>

<script>
import ResumeCard from "@/components/ResumeCard.vue"
import GlobalHeader from '@/components/GlobalHeader.vue'
import GlobalMessage from '@/components/GlobalMessage.vue'

const sampleData = [
  {
    id: 1,
    name: "Jollof Rice",
    picture: "/images/food-1.jpeg",
    ingredients: "Beef, Tomato, Spinach",
    difficulty: "easy",
    prep_time: 15,
    prep_guide:
      "Lorem ipsum dolor sit amet consectetur adipisicing elit. Omnis, porro. Dignissimos ducimus ratione totam fugit officiis blanditiis exercitationem, nisi vero architecto quibusdam impedit, earum "
  },
  {
    id: 2,
    name: "Macaroni",
    picture: "/images/food-2.jpeg",
    ingredients: "Beef, Tomato, Spinach",
    difficulty: "easy",
    prep_time: 15,
    prep_guide:
      "Lorem ipsum dolor sit amet consectetur adipisicing elit. Omnis, porro. Dignissimos ducimus ratione totam fugit officiis blanditiis exercitationem, nisi vero architecto quibusdam impedit, earum "
  },
  {
    id: 3,
    name: "Fried Rice",
    picture: "/images/banner.jpg",
    ingredients: "Beef, Tomato, Spinach",
    difficulty: "easy",
    prep_time: 15,
    prep_guide:
      "Lorem ipsum dolor sit amet consectetur adipisicing elit. Omnis, porro. Dignissimos ducimus ratione totam fugit officiis blanditiis exercitationem, nisi vero architecto quibusdam impedit, earum "
  }
];

export default {
  head() {
    return {
      title: "Resumes list"
    };
  },
  components: {
    ResumeCard,
    GlobalHeader,
    GlobalMessage
  },
  data() {
    return {
      resumes: []
    };
  },
  created: function () {
    let data = sampleData;
    this.resumes = data
  },
  methods: {
    deleteResume(recipe_id) {
      console.log(deleted `${resume.id}`)
    }
  }
};
</script>

<style scoped>
</style>
