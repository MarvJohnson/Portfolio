<template>
  <div class="technologies">
    <h3 class="section-label">Technologies I know</h3>
    <div class="padder">
      <Technology v-for="(technology, index) in technologies" :key="index" :icon="technology.icon" :label="technology.label" />
    </div>
  </div>
</template>

<script>
import Technology from './Technology'

export default {
  name: 'Technologies',
  components: {
    Technology
  },
  data: () => ({
    technologies: [
      { icon: ['fab', 'html5'], label: 'HTML5' },
      { icon: ['fab', 'css3-alt'], label: 'CSS3' },
      { icon: ['fab', 'node-js'], label: 'Javascript' },
      { icon: ['fab', 'vuejs'], label: 'Vue' },
      { icon: ['fab', 'react'], label: 'React' },
      { icon: ['fab', 'trello'], label: 'Trello' },
      { icon: ['fab', 'html5'], label: 'HTML5' },
      { icon: ['fab', 'css3-alt'], label: 'CSS3' },
      { icon: ['fab', 'node-js'], label: 'Javascript' },
      { icon: ['fab', 'html5'], label: 'HTML5' },
      { icon: ['fab', 'css3-alt'], label: 'CSS3' },
      { icon: ['fab', 'node-js'], label: 'Javascript' },
    ]
  })
}
</script>

<style>
  .technologies {
    font-size: 1rem;
  }

  .technologies > div {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    text-align: center;
    gap: 1em;
  }
</style>