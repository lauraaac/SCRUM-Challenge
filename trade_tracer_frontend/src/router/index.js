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
  },
  {
    path: '/stocks',
    name: 'StockGraphs',
    component: StockGraphs,
  },
  {
    path: '/stock',
    name: 'StockByDatesGraph',
    component: StockByDatesGraph,
  },
  {
    path: '/cryptos',
    name: 'CryptoGraphs',
    component: CryptoGraphs,
  },
  {
    path: '/crypto',
    name: 'CryptoByDatesGraph',
    component: CryptoByDatesGraph,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;