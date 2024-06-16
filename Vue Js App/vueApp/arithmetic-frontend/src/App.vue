<template>
  <div id="app">
    <h1>Arithmetic Operations</h1>
    <form @submit.prevent="calculate">
      <input type="number" v-model="num1" placeholder="Number 1" required />
      <input type="number" v-model="num2" placeholder="Number 2" required />
      <select v-model="operation">
        <option value="add">Add</option>
        <option value="subtract">Subtract</option>
        <option value="multiply">Multiply</option>
        <option value="divide">Divide</option>
      </select>
      <button type="submit">Calculate</button>
    </form>
    <div v-if="result !== null">Result: {{ result }}</div>
    <div v-if="error" class="error">Error: {{ error }}</div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
  data() {
    return {
      num1: null,
      num2: null,
      operation: 'add',
    };
  },
  computed: {
    ...mapState(['result', 'error']),
  },
  methods: {
    ...mapActions(['performOperation']),
    calculate() {
      this.performOperation({
        operation: this.operation,
        num1: this.num1,
        num2: this.num2,
      });
    },
  },
};
</script>

<style>
#app {
  max-width: 400px;
  margin: 50px auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}
.error {
  color: red;
  margin-top: 10px;
}
</style>
