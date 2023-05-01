import {
  createRouter,
  createWebHistory,
  RouteRecordRaw,
} from 'vue-router';
const routes: Array<RouteRecordRaw> = [
  // {
  //   path: '/',
  //   redirect: '/screen',
  // },
  {
    path: '/',
    name: 'screen',
    component: () => import('../pages/screen/index.vue')
  },
  {
    path: '/404',
    name: 'NotFond',
    component: () => import('../pages/404/NoFondPage.vue')
  },
];

const index = createRouter({
  history: createWebHistory(),
  routes,
});
export default index;
