import { createRouter, createWebHashHistory } from 'vue-router'

import EmployeesView from '../views/EmployeesView.vue'
import HomeView from '../views/HomeView.vue'
import LeadsView from '../views/LeadsView.vue'
import LoginForm from '../components/LoginForm.vue'
import RegisterForm from '../components/RegisterForm.vue'
import store from '@/store'

const routes = [
  {
    path: '/login',
    name: 'LoginForm',
    component: LoginForm
  },
  {
    path: '/register',
    name: 'RegisterForm',
    component: RegisterForm
  },
  {
    path: '/',
    name: 'HomeView',
    component: HomeView,
    meta: { requiresAuth: true } // Protect route
  },
  {
    path: '/employees',
    name: 'EmployeesView',
    component: EmployeesView,
    meta: { requiresAuth: true } // Protect route
  },
  {
    path: '/leads',
    name: 'LeadsView',
    component: LeadsView,
    meta: { requiresAuth: true } // Protect route
  },
  
];

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const isAuthenticated = store.getters.isAuthenticated;

  console.log('isAuthenticated', isAuthenticated);

  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!isAuthenticated) {
      next('/login');
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router
