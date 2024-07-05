<template>
    <v-dialog :model-value="dialog" max-width="600px" persistent>
      <v-card>
        <v-card-title>
          <span class="headline">Lead Filters</span>
        </v-card-title>
        <v-card-text>
          <v-container>
             
            <v-row>
              <v-col cols="12" sm="6">
                <v-text-field clearable v-model="filters.description" label="Description"></v-text-field>
              </v-col>
              <v-col cols="12" sm="6">
                <v-text-field clearable v-model="filters.raw_json" label="Raw Json"></v-text-field>
              </v-col>
            </v-row>

            <v-row>
              <v-col cols="12" sm="5">
                <v-text-field clearable v-model="filters.url" label="Company URL" hint="www.example.com/page"></v-text-field>
              </v-col>
              
              <v-col cols="12" sm="3">
                <v-text-field v-model="filters.urn" label="URN No." type="number"></v-text-field>
              </v-col>
              <v-col cols="12" sm="4">
                <v-checkbox
                  v-model="filters.is_demo_lead"
                  label="Is demo lead?"
                    ></v-checkbox>
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
          company_name: '',
          description: '',
          url: '',
          raw_json: '',
          is_demo_lead: false,
          urn: null,
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
        this.$emit('apply-filters', Object.assign({}, this.filters));
        this.closeDialog();
      }
    },
    watch:{
      dialog:{
        immediate: true,
        deep: true,
        handler(newVal){
          console.log("LeadDialog watcher", newVal)
        }
      }
    }
  };
  </script>
  