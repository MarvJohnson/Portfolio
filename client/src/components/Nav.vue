<template>
  <nav>
    <div class="nav-top">
      <p>MJ</p>
    </div>
    <div class="nav-options">
      <a href="#">Profile</a>
      <a href="#">Technologies</a>
      <a href="#">Resume</a>
      <a href="#">About</a>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'Nav'
}
</script>

<style>
  nav {
    display: flex;
    justify-content: space-between;
    border-bottom: 1px solid rgba(0, 0, 0, .2);
  }

  .nav-top {
    box-shadow: 0 0 5px 0 rgba(0, 0, 0, 0.3);
  }
</style>