<template>
  <main class="container my-5">
    <div class="row">
      <div class="col-12 text-center my-3">
        <h2 class="mb-3 display-4 text-uppercase">{{ resume.name }}</h2>
      </div>
      <div class="col-md-6 mb-4">
        <img
          class="img-fluid"
          style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
          :src="resume.picture"
          alt
        >
      </div>
      <div class="col-md-6">
        <div class="resume-details">
          <h4>Ingredients</h4>
          <p>{{ resume.ingredients }}</p>
          <h4>Preparation time ⏱</h4>
          <p>{{ resume.prep_time }} mins</p>
          <h4>Difficulty</h4>
          <p>{{ resume.difficulty }}</p>
          <h4>Preparation guide</h4>
          <textarea class="form-control" rows="10" v-html="resume.prep_guide" disabled />
        </div>
      </div>
    </div>
  </main>
</template>

<script>
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
      title: "View Resume"
    };
  },
  created: function () {
    let data = sampleData;
    let id = this.$route.params.resumeId;
    this.resume = data[id - 1]
  },
  data() {
    return {
      resume: {
        name: "",
        picture: "",
        ingredients: "",
        difficulty: "",
        prep_time: null,
        prep_guide: ""
      }
    };
  }
};
</script>

<style scoped>
</style>
