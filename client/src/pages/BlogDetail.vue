<template>
  <div class="blog-detail">
    <h1>{{ blogPost.title }}</h1>
    <h2>{{ blogPost.topic }}</h2>
    <section v-for="(section, sectionIndex) in blogPost.sections" :key="sectionIndex">
      <BlogPostContent v-for="(content, contentIndex) in section.contents" :key="contentIndex" :contentInfo="content" />
    </section>
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
      console.log(res);
    }
  }
}
</script>

<style>

</style>