import { createRouter, createWebHistory } from 'vue-router';
import Home from './pages/Home';
import Blog from './pages/Blog';
import BlogDetail from './pages/BlogDetail';

const routes = [
  { path: '/', component: Home, name: 'home' },
  { path: '/blog', component: Blog, name: 'blog' },
  { path: '/blog/:id', component: BlogDetail, name: 'blog_detail' }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
