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
      <ResultsTable :results="employees" :filters="filters" />
    </div>
    <employee-dialog
      v-model:dialog="dialog"
      @apply-filters="applyFilters"
    ></employee-dialog>
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar.vue';
import EmployeeDialog from '@/components/EmployeeDialog.vue';
import { apiCall } from '@/utils/api';
import ResultsTable from '@/components/ResultsTable.vue';
import { exportData } from '@/utils/exportData';


export default {
  name: 'EmployeesView',
  components: {
    SearchBar,
    EmployeeDialog,
    ResultsTable
  },
  data() {
    return {
      searchText: 'Search for employees, etc...',
      employees: [],
      filters: {},
      dataType: 'employees',
      headers: [
        { text: 'First Name', value: 'first_name' },
        { text: 'Last Name', value: 'last_name' },
        // Add more headers based on your data
      ],
      dialog: false
    };
  },
  mounted() {
    this.fetchEmployees();
  },
  methods: {
    exportResults(selectedFileType) {
      exportData(this.employees, `${this.dataType}_results`, selectedFileType);
    },
    applyFilters(filters) {
      // Handle updates to filters received from child component
      this.filters = Object.assign(this.filters, filters); // Create a shallow copy
      this.fetchEmployees();
    },
    async fetchEmployees() {
      let filters = this.filters
      console.log("fetchEmployees filters", filters);
      try {
        if (filters.raw_json) {
          filters.raw_json = JSON.parse(filters.raw_json);
        }
        this.employees = await apiCall('/employees', filters);
      } catch (error) {
        console.error('Error fetching employees:', error);
      }
    },
    search(query) {
      this.filters['name'] = query
      this.fetchEmployees();
    },
    openDialog() {
      this.dialog = true;
    }
  }
};
</script>
