<template>
  <div>
    <p ref="paragraph" v-if="contentInfo.type === 'PARAGRAPH'"></p>
    <img :src="contentInfo.content" alt="" v-if="contentInfo.type === 'IMAGE'">
    <pre v-if="contentInfo.type === 'CODE'">{{ contentInfo.content }}</pre>
  </div>
</template>

<script>
export default {
  name: 'BlogPostContent',
  props: {
    contentInfo: Object
  },
  mounted(){
    this.formatParagraph();
  },
  methods: {
    formatParagraph(){
      const paragraph = this.$refs.paragraph;

      if (!paragraph) return;

      let content = this.contentInfo.content;
      const lists = [...content.matchAll(/(?<!\(.*\))\[(.*)]/gm)];

      if (lists.length > 0) {
        for (let i = 0; i < lists.length; i++) {
          let currentList = lists[i][1].split(',');
          // console.log(currentList);
          let list = '<ul>__insert__</ul>';
          let items = '';

          for (let j = 0; j < currentList.length; j++) {
            items += `<li>${currentList[j]}</li>`;
          }
          
          list = list.replace('__insert__', items);
          content = content.replace(lists[i][0], list);
        }
      }

      content = content.replace(/\(([\w\d\s]+)\)\[([\w\d\s/:.%\-~#=]+)\]/gm, '<a href="$2" target="_blank">$1</a>');

      // console.log(content);
      paragraph.innerHTML = content;
    }
  }
}
</script>

<style scoped>
  p {
    color: var(--text1);
  }

  pre {
    background-color: var(--surface2);
    border-radius: 10px;
    padding: 1rem;
    white-space: pre-wrap;
    word-wrap: break-word;
  }
</style>