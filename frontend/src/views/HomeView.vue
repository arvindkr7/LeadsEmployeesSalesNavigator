<template>
    <div class="ma-3">
      <search-bar
        :searchText="searchText"
        :showDropdown="true"
        :searchTypes="searchTypes"
        @search="search"
        @searchTypeChange="searchTypeChange"
        @openDialog="openDialog"
        @exportResults="exportResults"
      ></search-bar>
      <div class="mx-3">
        <ResultsTable :results="results" :filters="filters" />
      </div>
    </div>
  </template>
  
  <script>
  import SearchBar from '@/components/SearchBar.vue';
  import ResultsTable from '@/components/ResultsTable.vue';
  import { apiCall } from '@/utils/api';
  import { exportData } from '@/utils/exportData';
  
  export default {
    name: 'HomeView',
    components: {
      SearchBar,
      ResultsTable
    },
    data() {
      return {
        searchText: 'Search for employees, leads, etc...',
        searchTypes: ['all', 'employees', 'leads'],
        results: [],
        searchType: 'all',
        filters: {},
        headers: [
          { text: 'Name', value: 'name' },
          { text: 'Type', value: 'type' },
          // Add more headers based on your data
        ]
      };
    },
    mounted() {
      this.fetchData();
    },
    methods: {
      exportResults(selectedFileType) {
        exportData(this.results, `${this.searchType}_results`, selectedFileType);
      },
      async fetchData(params = {}) {
        try {
          if (this.searchType === 'all') {
            this.results = await apiCall('/search', params);
          } else if (this.searchType === 'employees') {
            this.results = await apiCall('/employees', params);
          } else if (this.searchType === 'leads') {
            this.results = await apiCall('/leads', params);
          }
        } catch (error) {
          console.error('Error fetching data:', error);
        }
      },
      search(query) {
        this.filters['keyword'] = query
        const params = {
          keyword: query,
          s_type: this.searchType
        };
        this.fetchData(params);
      },
      searchTypeChange(type) {
        this.searchType = type;
        this.fetchData();
      },
      openDialog() {
        // Open dialog for additional filters
      }
    }
  };
  </script>
  