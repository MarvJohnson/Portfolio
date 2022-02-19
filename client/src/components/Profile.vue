<template>
  <div id="profile-anchor" class="profile">
    <img src="@/assets/portrait.png" alt="">
    <h2>Marvel Johnson</h2>
    <div class="profile-section">
      <h3>Title</h3>
      <p>Full-Stack Web Developer</p>
    </div>
    <div class="profile-section">
      <h3>Background</h3>
      <p class="background-text">
        I am a software engineer in pursuit of providing meaningful experiences at scale and driven by a passion for programming.
      </p>
      <p class="background-text">My work as a banker helped nurture an obsession for providing service as it pertains to individuals and their specific needs.
        This resulted in greater creativity when it comes to working through unique predicaments. The time I spent in a management role heightened my aptitude towards teamwork, strengthened my skill at delegating tasks, and improved my interpersonal relationship development competency.</p>
    </div>

    <div class="profile-footer">
      <a href="#resume-anchor">
        <button class="resume-btn action-btn">Resume</button>
      </a>
      <div class="social-btn-container">
        <a href="https://www.linkedin.com/in/marvel-johnson/" target="_blank" class="fa fa-brands fa-linkedin"></a>
        <a href="https://github.com/MarvJohnson" target="_blank" class="fa fa-brands fa-github"></a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Profile'
}
</script>

<style scoped>
  .profile {
    margin: 1rem;
    padding: 1rem;
    border: 1px solid rgba(0, 0, 0, 0.5);
  }

  .profile-section + .profile-section {
    margin-top: 1em;
  }

  img {
    display: block;
    margin: 0 auto;
    border-radius: 50%;
    border: 1px solid #000;
    max-width: 400px
  }

  .resume-btn {
    display: block;
    margin-top: 5em;
    width: 100%;
    height: 2em;
  }

  .profile-footer {
    max-width: 400px;
    margin: 0 auto;
  }

  .social-btn-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    height: 3rem;
    justify-items: center;
    align-items: center;
  }

  .social-btn-container a {
    color: var(--text1);
    font-size: 1.5rem;
    transition: transform 0.1s;
  }

  .social-btn-container a:hover {
    transform: scale(1.5);
  }

  h3,
  p {
    margin: 0;
  }

  .background-text {
    text-align: justify;
  }

  .background-text + .background-text {
    margin-top: 1em;
  }
</style>