<template>
  <div id="resumecard">
    <b-card :title="resume.companyName" :img-src="resume.picture" img-top>
      <b-card-text>
        {{ resume.term }}
      </b-card-text>
      <b-card-text>
        <strong>プロジェクト:</strong><br>{{ resume.project }}
      </b-card-text>
      <b-button-group>
        <b-row>
          <b-col md=4>
            <b-button pill variant="success" :to="`/resumes/${resume.id}`"> View </b-button>
          </b-col>
          <b-col md=4>
            <b-button pill variant="primary" :to="`/resumes/${resume.id}/edit`"> Edit </b-button>
          </b-col>
          <b-col md=4>
            <b-button pill variant="danger" @click="onDelete(resume.id)">Delete</b-button>
          </b-col>
        </b-row>
      </b-button-group>
    </b-card>
  </div>
</template>

<script>
export default {
    props: ["resume", "onDelete"]
};
</script>

<style>
#resumecard {
    box-shadow: 0 1rem 1.5rem rgba(0,0,0,.6);
}
</style>
