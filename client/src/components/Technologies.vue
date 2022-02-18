<template>
  <div class="technologies">
    <h3>Technologies I know</h3>
    <div>
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
      { icon: "['fas', fa-brands fa-html5]", label: 'HTML5' },
      { icon: "['fas', fa-brands fa-css3-alt]", label: 'CSS3' },
      { icon: "['fas', fa-brands fa-js]", label: 'Javascript' },
      { icon: "['fas', fa-brands fa-css3-alt]", label: 'CSS3' },
      { icon: "['fas', fa-brands fa-js]", label: 'Javascript' },
      { icon: "['fas', fa-brands fa-css3-alt]", label: 'CSS3' },
      { icon: "['fas', fa-brands fa-js]", label: 'Javascript' },
      { icon: "['fas', fa-brands fa-css3-alt]", label: 'CSS3' },
      { icon: "['fas', fa-brands fa-js]", label: 'Javascript' },
      { icon: "['fas', fa-brands fa-css3-alt]", label: 'CSS3' },
      { icon: "['fas', fa-brands fa-js]", label: 'Javascript' },
      { icon: "['fas', fa-brands fa-js]", label: 'Javascript' },
    ]
  })
}
</script>

<style>
  .technologies {
    font-size: 1rem;
  }

  .technologies > h3 {
    border-bottom: 1px solid var(--surface1);
    padding-bottom: 0.2em;
    margin: 1em;
  }

  .technologies > div {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    text-align: center;
    gap: 1em;
    margin: 0 1rem;
  }
</style>