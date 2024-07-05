<template>
  <div class="ma-3">
    <search-bar
      :searchText="searchText"
      :showDropdown="false"
      @search="search"
      @openDialog="openDialog"
      @exportResults="exportResults"
    ></search-bar>
    <div class="mx-3">
      <ResultsTable :headers="headers" :results="leads" :filters="filters" />
    </div>
    <lead-dialog
       v-model:dialog="dialog"
      @apply-filters="applyFilters"
    ></lead-dialog>
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar.vue';
import LeadDialog from '@/components/LeadDialog.vue';
import ResultsTable from '../components/ResultsTable.vue';
import { apiCall } from '@/utils/api';
import { exportData } from '@/utils/exportData';

export default {
  name: 'LeadsView',
  components: {
    SearchBar,
    LeadDialog,
    ResultsTable
  },
  data() {
    return {
      leads: [],
      searchText: 'Search for leads, etc...',
      filters: {},
      dataType: 'leads',
      dialog: false,
      headers:[ 
        'linkedin_url',
        'is_demo_lead',
        'description',
        'n_employees',
        'raw_json',
        'company_name',
        'url',
        'urn',
        'campaign_id'
      ]

  };
  },
  mounted() {
    this.fetchLeads();
  },
  methods: {
    exportResults(selectedFileType) {
      exportData(this.leads, `${this.dataType}_results`, selectedFileType);
    },
    async fetchLeads() {
      let filters = this.filters
      try {
        if (filters.raw_json) {
          filters.raw_json = JSON.parse(filters.raw_json);
        }else if(filters.raw_json == '') {
          filters.raw_json = {};
        }
        console.log("fetchLeads filters", filters);
        this.leads = await apiCall('/leads', filters);
        let first_row = this.leads[0];
        const resultArray = [];
          for (const key in first_row) {
            
            resultArray.push({ text: key, value: key });
          
        }
        // this.headers = resultArray
        console.log("leads", first_row, resultArray);
      } catch (error) {
        console.error('Error fetching leads:', error);
      }
    },
    applyFilters(filters ={}){
      this.filters = Object.assign(this.filters, filters); // Create a shallow copy
      this.fetchLeads();
    },
    search(query) {
      this.filters['company_name'] = query, // Adjust based on your search logic
      this.fetchLeads();
    },
    openDialog() {
      this.dialog = true;
    },
    closeDialog() {
      this.dialog = false;
    }

  },
  computed:{
    headers2(){
      let first_row = this.leads[0];
        const resultArray = [];
          for (const key in first_row) {
            
            resultArray.push({ text: key, value: key });
          
      }
      return resultArray;
    }
  }
};
</script>
