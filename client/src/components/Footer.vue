<template>
  <footer class="surface1">
    <p>Made by Marvel Johnson</p>
  </footer>
</template>

<script>
export default {
  name: 'Footer'
}
</script>

<style>
  footer {
    display: flex;
    justify-content: center;
    font-style: italic;
    align-items: center;
    margin-top: 5rem;
    height: 4rem;
    color: var(--text2);
  }

  footer p {
    margin: 0;
  }
</style>