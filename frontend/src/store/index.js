import { apiCall } from '@/utils/api';
import axios from 'axios';
import { createStore } from 'vuex';

export default createStore({
  state: {
    user: null,
    token: localStorage.getItem('token') || null,
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    },
    setToken(state, token) {
      state.token = token;
    },
    logout(state) {
      state.user = null;
      state.token = null;
      localStorage.removeItem('token');
    }
  },
  actions: {
    async register({commit}, { username, password }) {
      commit('')
      console.log(username + ' ' + password);
      const response = await apiCall('/register', { username, password });
      return response.data;
    },
    async login({ commit }, { username, password }) {
      const response = await apiCall('/login', { username, password });
      commit('setToken', response.access);
      localStorage.setItem('token', response.access);
      axios.defaults.headers.common['Authorization'] = `Bearer ${response.access}`;
      const user = { username };
      commit('setUser', user);
      return user;
    },
    logout({ commit }) {
      commit('logout');
      delete axios.defaults.headers.common['Authorization'];
    },
  },
  getters: {
    isAuthenticated: state => !!state.token,
    getUser: state => state.user,
  },
});
