<template>
      <v-row>
        <v-col>
          <v-text-field
            variant="solo"
            prepend-inner-icon="mdi-magnify"
            v-model="searchQuery"
            :label="searchText"
            @input="onSearch"
          ></v-text-field>
        </v-col>
        <v-col sm="2" v-if="showDropdown">
          <v-select
            variant="solo"
            v-model="searchType"
            :items="searchTypes"
            label="Search Type"
            @change="onSearchTypeChange"
          ></v-select>
         
        </v-col>
        <v-col sm="2" v-else>
          <v-btn block id="btn-filter" size="x-large" @click="openDialog">Filters <v-icon
          icon="mdi-filter"
          end
        ></v-icon></v-btn>
        </v-col>
        <v-col sm="2">
            <v-select
              variant="solo"
              v-model="selectedFileType"
              :items="fileTypes"
              label="Select file type"
            ></v-select>
    
        </v-col>
        <v-col sm="2">
          <v-btn block id="btn-filter" size="x-large" @click="exportResults">Export <v-icon
          icon="mdi-file"
          end
        ></v-icon></v-btn>
        </v-col>
      </v-row>
      
  </template>
  
  <script>
  export default {
    props: {
      showDropdown: Boolean,
      searchTypes: Array,
      searchText: String,
    },
    data() {
      return {
        searchQuery: '',
        searchType: 'all',
        selectedFileType: 'csv',
        fileTypes: ['csv', 'excel']
      };
    },
    methods: {
      onSearch() {
        this.$emit('search', this.searchQuery);
      },
      onSearchTypeChange() {
        this.$emit('searchTypeChange', this.searchType);
      },
      openDialog() {
        this.$emit('openDialog');
      },
      exportResults(){
        this.$emit('exportResults', this.selectedFileType);
      }
    }
  };
  </script>

  <style scoped>
  #btn-filter{
    height: 56px;
  }


</style>
  