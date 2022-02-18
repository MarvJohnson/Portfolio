<template>
  <nav>
    <Transition>
      <button class="hamburger main fas fa-bars" @click="toggleMobileSlideout" v-if="!navMobileSlideout"></button>
    </Transition>
    <Transition>
      <div class="nav-mobile surface1" @click="toggleMobileSlideout" v-if="navMobileSlideout">
        <button class="hamburger fas fa-bars"></button>
        <ul class="nav-options">
          <li><a href="#">About Me</a></li>
          <li><a href="#">Technologies</a></li>
          <li><a href="#">Projects</a></li>
          <li><a href="#">Resume</a></li>
        </ul>
      </div>
    </Transition>
    <div class="nav-desktop">
      <div class="nav-top">
        <p>MJ</p>
      </div>
      <div class="nav-options">
        <a href="#">Profile</a>
        <a href="#">Technologies</a>
        <a href="#">Resume</a>
        <a href="#">About</a>
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
  }

  .nav-mobile {
    position: absolute;
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
    box-shadow: 0 0 5px 0 rgba(0, 0, 0, 0.3);
  }

  .nav-top p {
    margin: 0;
  }

  .hamburger {
    background-color: unset;
    border: none;
    font-size: 2rem;
    color: var(--text1);
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