<template>
  <div class="resume">
    <h3 class="section-label">Resume</h3>
    <div class="padder">
      <img src="@/assets/resume.png" alt="">
      <button @click="downloadResume">Download</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import resume from '../assets/resume.png'

export default {
  name: 'Resume',
  methods: {
    async downloadResume(){
      const result = await axios.get(resume, { responseType: 'blob' });
      const blob = new Blob([result.data], { type: 'image/png' });
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
  }
</style>