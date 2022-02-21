<template>
  <div class="blog">
    <h1>Blog Posts</h1>
    <div class="post-container">
      <ol>
        <li v-for="(post, index) in posts" :key="index">
          <router-link :to="`/blog/${post.id}`" class="blog-link">
            {{ post.title }}
          </router-link>
        </li>
      </ol>
    </div>
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
    }
  }
}
</script>

<style scoped>
  .blog {
    text-align: center;
    min-height: 100vh;
  }

  h1 {
    margin-top: 5rem;
    font-size: 2rem;
  }

  .post-container {
    width: 200px;
    white-space: nowrap;
    margin: 0 auto;
    text-align: left;
  }

  li, .blog-link {
    font-size: 1.2rem;
    text-decoration: underline;
    text-underline-offset: 0.5rem;
  }
</style>