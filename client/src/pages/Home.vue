<template>
  <div class="home">
    <main>
      <Profile />
      <section>
        <Technologies />
      </section>
      <section>
        <Projects />
      </section>
      <section>
        <Resume />
      </section>
    </main>
  </div>
</template>

<script>
import Profile from '../components/Profile'
import Technologies from '../components/Technologies'
import Projects from '../components/Projects'
import Resume from '../components/Resume'

export default {
  name: 'Home',
  components: {
    Profile,
    Technologies,
    Projects,
    Resume,
  }
}
</script>

<style scoped>
  main {
    max-width: 800px;
    margin: 0 auto;
  }

  section {
    margin: 10rem 0;
  }
</style>