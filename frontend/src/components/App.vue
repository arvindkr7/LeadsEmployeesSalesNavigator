<template>
  <v-app>
    <app-bar></app-bar>
    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
import AppBar from '@/components/AppBar.vue';

export default {
  components: {
    AppBar
  }
};
</script>
