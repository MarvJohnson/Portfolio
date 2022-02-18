<template>
  <div class="resume">
    <img src="@/assets/resume.png" alt="">
    <button @click="downloadResume">Download</button>
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
  .resume {
    padding: 0 1em;
  }

  img {
    width: 100%;
  }
</style>