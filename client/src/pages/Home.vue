<template>
  <div class="home">
    <Nav />
    <main>
      <Profile />
      <Technologies />
      <Projects />
      <Resume />
    </main>
    <Footer />
  </div>
</template>

<script>
import Nav from '../components/Nav'
import Profile from '../components/Profile'
import Technologies from '../components/Technologies'
import Projects from '../components/Projects'
import Resume from '../components/Resume'
import Footer from '../components/Footer'

export default {
  name: 'Home',
  components: {
    Nav,
    Profile,
    Technologies,
    Projects,
    Resume,
    Footer
  }
}
</script>

<style>
  @import url("../styles/global.css");

  main {
    max-width: 600px;
  }
</style>