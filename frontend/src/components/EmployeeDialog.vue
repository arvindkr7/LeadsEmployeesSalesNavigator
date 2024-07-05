<template>
    <v-dialog :model-value="dialog" max-width="600px" persistent>
      <v-card>
        <v-card-title>
          <span class="headline">Employee Filters</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12" sm="6">
                <v-text-field clearable v-model="filters.first_name" label="First Name"></v-text-field>
              </v-col>
              <v-col cols="12" sm="6">
                <v-text-field clearable v-model="filters.last_name" label="Last Name"></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" sm="12">
                <v-text-field clearable v-model="filters.raw_json" label="Raw Json"></v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="closeDialog">Cancel</v-btn>
          <v-btn color="blue darken-1" text @click="applyFilters">Apply</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </template>
  
  <script>
  export default {
    props: {
      dialog: {
        type: Boolean,
        required: true
      }
    },
    data() {
      return {
        filters: {
          first_name: '',
          last_name: '',
          raw_json: '',
        }
      };
    },
    methods: {
      updateDialog(value) {
        this.$emit('update:dialog', value);
      },
      closeDialog() {
        this.$emit('update:dialog', false);
      },
      applyFilters() {
         // Convert raw_json string to JSON object if it exists
      
        console.log("employee dialog filters", this.filters)
        this.$emit('apply-filters', Object.assign({}, this.filters));
        this.closeDialog();
      }
    }
  };
  </script>
  