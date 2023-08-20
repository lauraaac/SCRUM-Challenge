import { createRouter, createWebHistory } from 'vue-router';
import StockGraphs from '@/components/StockGraphs.vue';

const routes = [
  {
    path: '/',
    name: 'StockGraphs',
    component: StockGraphs,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;