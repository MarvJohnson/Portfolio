<template>
  <div class="profile">
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

    <button class="resume-btn">Resume</button>
    <a href="#" class="fa fa-brands fa-linkedin"></a>
    <a href="#" class="fa fa-brands fa-github"></a>
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
  }

  .resume-btn {
    display: block;
    margin-top: 5em;
    width: 100%;
    height: 2em;
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