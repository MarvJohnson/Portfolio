<template>
  <div class="blog">
    <router-link v-for="(post, index) in posts" :key="index" :to="`/blog/${post.id}`">
      {{ post.title }}
    </router-link>
  </div>
</template>

<script>
import { getBlogPosts } from '../services/BlogServices';

export default {
  name: 'Blog',
  data: () => ({
    posts: []
  }),
  mounted(){
    this.getBlogPosts();
  },
  methods: {
    async getBlogPosts(){
      const res = await getBlogPosts();
      this.posts = res;
      console.log(res);
    }
  }
}
</script>

<style>

</style>