<template>
    <v-app-bar app color="primary" dark>
      <v-toolbar-title>
        <div class="align-center">
        <img :src="require('@/assets/logo.png')" alt="Logo" height="25" contain/>
        &nbsp;
         Sales Navigator
        </div>
        
      </v-toolbar-title>
      <div v-if="isAuthenticated">
      <v-tabs v-model="currentTab">
        <v-tab to="/"> <v-icon icon="mdi-home"></v-icon>&nbsp; Home</v-tab>
        <v-tab to="/employees"> <v-icon icon="mdi-account"></v-icon>&nbsp; Employees</v-tab>
        <v-tab to="/leads"> <v-icon icon="mdi-domain"></v-icon>&nbsp; Leads</v-tab>
        <v-tab><v-btn variant="outlined" class="mr-4" @click="redirectToExternalLink">API Docs 
        <v-icon
          icon="mdi-wrench"
          end
        ></v-icon></v-btn></v-tab>
        <v-tab><v-btn variant="plain" class="mr-4" @click="logout">Log Out
        <v-icon
          icon="mdi-logout"
          end
        ></v-icon></v-btn></v-tab>
        
      </v-tabs>
      <v-spacer></v-spacer>
      </div>
      <v-btn v-else variant="outlined" :to="'/login'" class="mr-4">Login</v-btn>
      <v-spacer></v-spacer>
    </v-app-bar>
  </template>
  
  <script>
  import { mapGetters } from 'vuex';
  import {useToast} from 'vue-toast-notification';
  export default {
    data() {
      return {
        currentTab: 0
      };
    },
    computed: {
    ...mapGetters(['isAuthenticated']),
  },
    methods: {
    redirectToExternalLink() {
      window.location.href = 'http://localhost:8000/api/docs';
    },
    logout() {
      this.$store.dispatch('logout');
      const toast = useToast();
      toast.success('Logout successful');
      this.$router.push('/login');
    }
  }

  };
  </script>

<style scoped>
.align-center {
  display: flex;
  margin: 0; /* Centers the image horizontally */
  align-items: center;
}
</style>
  