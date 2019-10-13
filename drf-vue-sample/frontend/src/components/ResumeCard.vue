<template>
  <div class="card resume-card">
    <img :src="resume.picture" class="card-img-top" >
    <div class="card-body">
      <h5 class="card-title">{{ resume.name }}</h5>
      <p class="card-text">
        <strong>Ingredients:</strong> {{ resume.ingredients }}
      </p>
      <div class="action-buttons">
        <router-link :to="`/resumes/${resume.id}`" class="btn btn-sm btn-success"> View </router-link>
        <router-link :to="`/resumes/${resume.id}/edit`" class="btn btn-sm btn-primary"> Edit </router-link>
        <button @click="onDelete(resume.id)"  class="btn btn-sm btn-danger">Delete</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
    props: ["resume", "onDelete"]
};
</script>

<style>
.recipe-card {
    box-shadow: 0 1rem 1.5rem rgba(0,0,0,.6);
}
</style>
