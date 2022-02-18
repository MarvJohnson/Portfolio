<template>
  <div class="resume">
    <img src="@/assets/resume.png" alt="">
    <a href="@/assets" download="resume"><button>Download</button></a>
  </div>
</template>

<script>
export default {
  name: 'Resume'
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