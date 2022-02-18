<template>
  <div class="technology">
    <font-awesome-icon :icon="icon"></font-awesome-icon>
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
    border: 1px solid rgba(0, 0, 0, 0.3);
  }
</style>