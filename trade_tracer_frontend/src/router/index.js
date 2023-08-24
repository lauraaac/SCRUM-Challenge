import { createRouter, createWebHistory } from 'vue-router';
import GraphsHome from '@/components/GraphsHome.vue';
import StockGraphs from '@/components/StockGraphs.vue';
import StockByDatesGraph from '@/components/StockByDatesGraph.vue'
import CryptoGraphs from '@/components/CryptoGraphs.vue'
import CryptoByDatesGraph from '@/components/CryptoByDatesGraph.vue'

const routes = [
  {
    path: '/',
    name: 'GraphsHome',
    component: GraphsHome,
    meta: {
      title: 'Trade Tracer',
    },
  },
  {
    path: '/stocks',
    name: 'StockGraphs',
    component: StockGraphs,
    meta: {
      title: 'All stocks',
    },
  },
  {
    path: '/stock',
    name: 'StockByDatesGraph',
    component: StockByDatesGraph,
    meta: {
      title: 'Single stock',
    },
  },
  {
    path: '/cryptos',
    name: 'CryptoGraphs',
    component: CryptoGraphs,
    meta: {
      title: 'All cryptocurrencies',
    },
  },
  {
    path: '/crypto',
    name: 'CryptoByDatesGraph',
    component: CryptoByDatesGraph,
    meta: {
      title: 'Single cryptocurrency',
    },
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  document.title = to.meta.title || 'Default Title';
  next();
});

export default router;