<template>
  <div class="technology">
    <img :src="icon" alt="">
    <p>{{ label }}</p>
  </div>
</template>

<script>
export default {
  name: 'Technology',
  props: {
    icon: String,
    label: String
  }
}
</script>

<style>
  .technology {
    display: grid;
    grid-template-rows: 1fr 3rem;
    border: 1px solid rgba(0, 0, 0, 0.3);
    padding: 0.5rem;
  }

  img {
    width: 100%;
  }
</style>