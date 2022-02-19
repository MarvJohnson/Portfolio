<template>
  <nav class="surface1">
    <Transition>
      <div class="hamburger main" @click="toggleMobileSlideout" v-if="!navMobileSlideout">
        <div class="hamburger-segment"></div>
        <div class="hamburger-segment"></div>
        <div class="hamburger-segment"></div>
      </div>
    </Transition>
    <Transition>
      <div class="nav-mobile surface1" v-if="navMobileSlideout">
        <div class="hamburger" @click="toggleMobileSlideout">
          <div class="hamburger-segment"></div>
          <div class="hamburger-segment"></div>
          <div class="hamburger-segment"></div>
        </div>
        <ul class="nav-options">
          <li><a href="#profile-anchor" @click="toggleMobileSlideout">Profile</a></li>
          <li><a href="#technologies-anchor" @click="toggleMobileSlideout">Technologies</a></li>
          <li><a href="#projects-anchor" @click="toggleMobileSlideout">Projects</a></li>
          <li><a href="#resume-anchor" @click="toggleMobileSlideout">Resume</a></li>
        </ul>
      </div>
    </Transition>
    <div class="nav-desktop">
      <div class="nav-top">
        <p>MJ</p>
      </div>
      <div class="nav-options">
        <a href="#profile-anchor">Profile</a>
        <a href="#technologies-anchor">Technologies</a>
        <a href="#projects-anchor">Projects</a>
        <a href="#resume-anchor">Resume</a>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'Nav',
  data: () => ({
    navMobileSlideout: false
  }),
  methods: {
    toggleMobileSlideout(){
      this.navMobileSlideout = !this.navMobileSlideout;
    }
  }
}
</script>

<style>
  nav {
    display: flex;
    flex-direction: column;
    justify-content: center;
    position: sticky;
    height: 48px;
    border-bottom: 1px solid rgba(0, 0, 0, .2);
  }

  .nav-desktop {
    display: none;
    justify-content: space-between;
    align-items: center;
    height: 100%;
  }

  .nav-desktop .nav-options {
    font-size: 1.3rem;
    padding-right: 1rem;
  }

  .nav-desktop .nav-options a {
    color: var(--text1);
    text-decoration: none;
  }

  .nav-desktop .nav-options a + a {
    margin-left: 1rem;
  }

  .nav-mobile {
    position: fixed;
    top: 0;
    left: 0;
    width: 95vw;
    height: 100vh;
    padding: 0.5rem;
    box-sizing: border-box;
    transform: translateX(0);
  }

 .nav-mobile ul {
   list-style: none;
   font-size: 1.3rem;
   margin-top: 2rem;
   padding: 0 1.1rem;
 }

  .nav-mobile a {
    text-decoration: none;
    color: var(--text1);
  }

  .nav-mobile ul li {
    padding-bottom: 0.5em;
    border-bottom: 1px solid var(--text1);
  }

  .nav-mobile ul li + li {
    margin-top: 0.5em;
  }

  .nav-mobile.v-enter-active {
    transition: transform 0.3s 0.2s ease-in-out;
  }

  .nav-mobile.v-leave-active {
    transition: transform 0.3s ease-in-out;
  }

  .nav-mobile.v-enter-from,
  .nav-mobile.v-leave-to {
    transform: translateX(-100%);
  }

  .nav-top {
    display: flex;
    justify-content: center;
    align-items: center;
    box-shadow: 0 0 5px 0 rgba(0, 0, 0, 0.5);
    width: 3rem;
    height: 100%;
  }

  .nav-top p {
    margin: 0;
    font-size: 1.5rem;
  }

  .hamburger {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    border: none;
    height: 1.7rem;
    width: 2rem;
    color: var(--text1);
  }

  .hamburger-segment {
    height: 1rem;
    transform: scaleY(0.5);
    background-color: white;
  }

  .hamburger.main {
    padding: 0.5rem;
  }

  .hamburger.main.v-enter-active,
  .hamburger.main.v-leave-active {
    transition: opacity 0.1s ease-in-out;
  }

  .hamburger.main.v-enter-from,
  .hamburger.main.v-leave-to {
    opacity: 0;
  }

  @media screen and (min-width: 700px) {
    .nav-mobile,
    .hamburger {
      display: none;
    }

    .nav-desktop {
      display: flex;
    }
  }
</style>