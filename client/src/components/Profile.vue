<template>
  <div class="profile">
    <img src="@/assets/portrait.png" alt="">
    <h2>Marvel Johnson</h2>
    <h3>Title</h3>
    <p>Full-Stack Web Developer</p>
    <h3>Background</h3>
    <p class="background-text">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Error veniam vel animi cum nihil ab possimus mollitia repellendus et, reiciendis illum fugiat iste debitis tempore dolore aliquam? Incidunt, magnam ratione.
    Quidem quis, ad reiciendis velit doloribus explicabo corrupti provident sequi soluta doloremque recusandae odio quibusdam praesentium, harum rem. Tempora, facere voluptate voluptatibus obcaecati doloribus possimus quisquam ex unde asperiores est.
    Quis atque nihil deleniti, aliquam porro laudantium exercitationem, dolor odio ipsa veritatis, repellat qui placeat iste velit molestiae ea beatae nostrum harum eos facilis quasi? Doloribus fugit excepturi vero aut?</p>
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

  img {
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
</style>