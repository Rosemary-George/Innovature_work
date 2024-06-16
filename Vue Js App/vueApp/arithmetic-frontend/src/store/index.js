import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    result: null,
    error: null,
  },
  mutations: {
    SET_RESULT(state, result) {
      state.result = result;
    },
    SET_ERROR(state, error) {
      state.error = error;
    },
  },
  actions: {
    async performOperation({ commit }, { operation, num1, num2 }) {
      try {
        const response = await axios.post(`http://localhost:8000/AuthenticationSystem/ArithmenticOperations/${operation}/`, { num1, num2 });
        commit('SET_RESULT', response.data.result);
        commit('SET_ERROR', null);
      } catch (error) {
        commit('SET_ERROR', error.response.data.error);
      }
    },
  },
  getters: {
    result: state => state.result,
    error: state => state.error,
  },
});
