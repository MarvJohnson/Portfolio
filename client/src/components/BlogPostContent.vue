<template>
  <p v-if="contentInfo.type === 'PARAGRAPH'">{{ contentInfo.content }}</p>
  <img v-else-if="contentInfo.type === 'IMAGE'" :src="contentInfo.content" alt="">
</template>

<script>
export default {
  name: 'BlogPostContent',
  props: {
    contentInfo: Object
  }
}
</script>

<style>

</style>