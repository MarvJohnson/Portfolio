<template>
  <div id="projects-anchor" class="projects">
    <h3 class="section-label">Projects</h3>
    <carousel :settings="carouselSettings">
      <slide v-for="project in projects" :key="project.name">
        <a :href="project.url" target="_blank">
          <img :src="project.image" alt="">
        </a>
      </slide>
      <template #addons>
        <navigation />
        <pagination />
      </template>
    </carousel>
  </div>
</template>

<script>
import exstudio_Thumbnail from '../assets/EXStudio_Thumbnail.png'
import gameofsnake_Thumbnail from '../assets/GameOfSnake_Thumbnail.jpg'
import moviedb_thumbnail from '../assets/MovieDB_Thumbnail.jpg'
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
    },
    projects: [
      { name: 'MovieDB', image: moviedb_thumbnail, description: '', url: 'http://marvel-moviedb.surge.sh/' },
      { name: 'EX Studio', image: exstudio_Thumbnail, description: '', url: 'https://ex-studio.herokuapp.com/landing' },
      { name: 'Game of Snake', image: gameofsnake_Thumbnail, description: '', url: 'http://marvel-game-of-snake.surge.sh/' },
    ]
  })
}
</script>

<style>
  .carousel__next,
  .carousel__prev {
    display: none;
  }

  .carousel__pagination {
    padding: 0;
  }

  .carousel  {
    margin: 0 1rem;
  }

  .carousel__pagination-button {
    background-color: var(--surface1);
  }

  .carousel__pagination-button--active {
    background-color: var(--surface2);
  }
</style>