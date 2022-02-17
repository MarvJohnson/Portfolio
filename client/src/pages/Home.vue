<template>
  <div class="home">
    <Nav />
    <main>

    </main>
    <footer>
      
    </footer>
  </div>
</template>

<script>
import Nav from '../components/Nav'
import Profile from '../components/Profile'
import Technologies from '../components/Techonologies'
import Projects from '../components/Projects'
import Resume from '../components/Resume'

export default {
  name: 'Home',
  components: {
    Nav,
    Profile,
    Technologies,
    Projects,
    Resume
  }
}
</script>

<style>

</style>