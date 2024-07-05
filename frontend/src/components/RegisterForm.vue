<template>
  <v-card
    class="mx-auto my-auto bg-primary"
    max-width="344"
    title="User Registration" rounded
  >
  <v-form @submit.prevent="register">
    <v-container>
      <v-text-field
        v-model="username"
        color="primary"
        label="Email"
        variant="underlined"
      ></v-text-field>

      <v-text-field
        v-model="password"
        type="password"
        color="primary"
        label="Password"
        placeholder="Enter your password"
        variant="underlined"
      ></v-text-field>

      <v-checkbox
        v-model="terms"
        color="secondary"
        label="I agree to site terms and conditions"
      ></v-checkbox>
    </v-container>

    <v-divider></v-divider>

    <v-card-actions>
      <v-spacer></v-spacer>

      <v-btn color="success" type="submit">
        Complete Registration
        <v-icon icon="mdi-chevron-right" end></v-icon>
      </v-btn>
    </v-card-actions>
    </v-form>
  </v-card>
</template>

<script>
import {useToast} from 'vue-toast-notification';
import 'vue-toast-notification/dist/theme-sugar.css';
export default {
  data() {
    return {
      username: '',
      password: '',
      terms: false,
    };
  },
  methods: {
    async register() {
      const toast = useToast();
      try {
        await this.$store.dispatch('register', { username: this.username, password: this.password });
        this.$router.push('/login');
      } catch (error) {
        console.error('Register error:', error);
        toast.error('Registration failed. Please try again.');
      }
    }
  }
};
</script>
