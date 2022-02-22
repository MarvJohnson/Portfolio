<template>
  <div class="blog-detail">
    <div class="post-container">
      <div class="description-container">
        <h1>{{ blogPost.title }}</h1>
      </div>
      <section v-for="(section, sectionIndex) in blogPost.sections" :key="sectionIndex">
        <h3>{{ section.title }}</h3>
        <BlogPostContent v-for="(content, contentIndex) in section.contents" :key="contentIndex" :contentInfo="content" />
      </section>
    </div>
  </div>
</template>

<script>
import { getBlogPostDetail } from '../services/BlogServices';
import BlogPostContent from '../components/BlogPostContent';

export default {
  name: 'BlogDetail',
  data: () => ({
    blogPost: {}
  }),
  components: {
    BlogPostContent
  },
  mounted(){
    this.getBlogPostDetail()
  },
  methods: {
    async getBlogPostDetail() {
      const blogPostId = parseInt(this.$route.params.id);
      const res = await getBlogPostDetail(blogPostId);
      this.blogPost = res;
    }
  }
}
</script>

<style scoped>
  .blog-detail {
    min-height: 100vh;
  }

  .description-container {
    margin: 5rem 0;
  }

  h1, h2, h3, p {
    margin: 0;
  }

  h1 {
    font-size: 2rem;
    margin-bottom: 0.2rem;
  }

  h2 {
    font-size: 0.9rem;
  }

  h3 {
    font-size: 1.2rem;
    margin-bottom: 1rem;
  }

  p {
    margin-bottom: 1rem;
  }

  .post-container {
    width: 60%;
    max-width: 600px;
    margin: 0 auto;
  }
</style>