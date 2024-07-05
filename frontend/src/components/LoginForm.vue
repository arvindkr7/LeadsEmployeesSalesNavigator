<template>
  <v-sheet class="m-auto" rounded>
    <v-card class="mx-auto my-auto px-6 py-8 bg-primary" max-width="344" title="Login to get started...">
      <v-form
        @submit.prevent="login"
      >
        <v-text-field
          v-model="username"
          :readonly="loading"
          :rules="[required]"
          class="mb-2"
          label="Email"
          clearable
        ></v-text-field>

        <v-text-field
          v-model="password"
          :readonly="loading"
          :rules="[required]"
          label="Password"
          type="password"
          placeholder="Enter your password"
          clearable
        ></v-text-field>

        <br>

        <v-btn
          :loading="loading"
          color="success"
          size="large"
          type="submit"
          variant="elevated"
          block
        >
          Sign In
        </v-btn>
      </v-form>

      <v-divider></v-divider>
      <v-btn class="mt-7" size="large" block variant="outlined" :to="'/register'">Register now</v-btn>
    </v-card>
  </v-sheet>
</template>
<script>
import {useToast} from 'vue-toast-notification';
import 'vue-toast-notification/dist/theme-sugar.css';
export default {
    data: () => ({
      form: false,
      username: null,
      password: null,
      loading: false,
    }),

    methods: {
      onSubmit () {
        if (!this.form) return
        this.loading = true
        setTimeout(() => (this.loading = false), 2000)
      },
      async login() {
        const toast = useToast();
      try {
        await this.$store.dispatch('login', { username: this.username, password: this.password });
        toast.success('Login successful');
        this.$router.push('/');
      } catch (error) {
        console.error('Login error:', error);
        toast.error('Login error: Invalid username or password');
      }
    },
      required (v) {
        return !!v || 'Field is required'
      },
    },
  }
</script>


