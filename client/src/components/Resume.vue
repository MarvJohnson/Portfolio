<template>
  <div id="resume-anchor" class="resume">
    <h3 class="section-label">Resume</h3>
    <div class="padder">
      <img src="@/assets/resume.png" alt="">
      <button @click="downloadResume('~/public')" class="download-resume-btn action-btn">Download</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Resume',
  data: () => ({
    publicPath: process.env.BASE_URL
  }),
  methods: {
    async downloadResume(){
      const result = await axios.get(`${this.publicPath}resume.docx`, { responseType: 'blob' });
      const blob = new Blob([result.data], { type: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document' });
      const link = document.createElement('a');
      link.href = URL.createObjectURL(blob);
      link.download = 'resume';
      link.click();
      URL.revokeObjectURL(link.href);
    }
  }
}
</script>

<style scoped>
  img {
    width: 100%;
    border: 3px solid var(--surface2);
  }

  .download-resume-btn {
    height: 2rem;
  }
</style>