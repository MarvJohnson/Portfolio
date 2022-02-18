<template>
  <div class="projects">
    <h3>Projects</h3>
    <carousel :settings="carouselSettings">
      <slide v-for="slide in 10" :key="slide">
        {{ slide }}
      </slide>
      <template #addons>
        <navigation />
        <pagination />
      </template>
    </carousel>
  </div>
</template>

<script>
import 'vue3-carousel/dist/carousel.css'
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel'

export default {
  name: 'Projects',
  components: {
    Carousel,
    Slide,
    Pagination,
    Navigation
  },
  data: () => ({
    carouselSettings: {
      itemsToShow: 1,
      wrapAround: true
    }
  })
}
</script>

<style>
  .projects > h3 {
    border-bottom: 1px solid var(--surface1);
    padding-bottom: 0.2em;
    margin: 1em;
  }

  .carousel__next,
  .carousel__prev {
    display: none;
  }

  .carousel__pagination {
    padding: 0;
  }
</style>