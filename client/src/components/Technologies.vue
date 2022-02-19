<template>
  <div id="technologies-anchor" class="technologies">
    <h3 class="section-label">Technologies I know</h3>
    <div class="padder">
      <Technology v-for="(technology, index) in technologies" :key="index" :icon="technology.icon" :label="technology.label" />
    </div>
  </div>
</template>

<script>
import Technology from './Technology'
import html from '../assets/html.png'
import css from '../assets/css.png'
import javascript from '../assets/javascriptbw.png'
import git from '../assets/git.png'
import django from '../assets/django.png'
import express from '../assets/express-squared.png'
import mongodb from '../assets/mongodb-icon-12.png'
import mongoose from '../assets/mongoose.png'
import node from '../assets/nodebw.png'
import postgresql from '../assets/postgresql.png'
import react from '../assets/reactbw.png'
import redux from '../assets/redux.png'
import sequelize from '../assets/sequelizebw.png'
import vue from '../assets/vuebw.png'

export default {
  name: 'Technologies',
  components: {
    Technology
  },
  data: () => ({
    technologies: [
      { icon: html, label: 'HTML5' },
      { icon: css, label: 'CSS3' },
      { icon: javascript, label: 'Javascript' },
      { icon: node, label: 'Node.js' },
      { icon: express, label: 'Express.js' },
      { icon: django, label: 'Django' },
      { icon: mongodb, label: 'MongoDB' },
      { icon: postgresql, label: 'PostgreSQL' },
      { icon: git, label: 'Git' },
      { icon: react, label: 'React' },
      { icon: redux, label: 'Redux' },
      { icon: sequelize, label: 'Sequelize' },
      { icon: vue, label: 'Vue' },
      { icon: mongoose, label: 'Mongoose' },
    ]
  })
}
</script>

<style>
  .technologies {
    font-size: 1rem;
  }

  .technologies > div {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    text-align: center;
    gap: 1em;
  }
</style>