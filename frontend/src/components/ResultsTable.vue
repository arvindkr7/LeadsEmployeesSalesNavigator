<template>
  <v-data-table :items="highlightedResults" item-key="id" variant="solo">
    <template v-slot:item="props">
      <tr>
        <td v-for="(value, key) in props.item" :key="key" v-html="formatValue(value, key)"></td>
      </tr>
    </template>
  </v-data-table>
</template>

<script>
export default {
  props: {
    results: {
      type: Array,
      required: true
    },
    filters: {
      type: Object,
      required: true
    }
  },
  methods: {
    highlightText(text, keyword) {
      console.log("highlightText", text, keyword);
      if (!keyword) return text;
      const regex = new RegExp(`(${keyword})`, 'gi');
      return text.replace(regex, '<span class="highlight">$1</span>');
    },
    formatValue(value, key) {
      console.log("formatValue", value, key);
      if (typeof value === 'string') {
        for (const filterKey in this.filters) {
          if (this.filters[filterKey]) {
            value = this.highlightText(value, this.filters[filterKey]);
          }
        }
      } else if (typeof value === 'object' && value !== null) {
        if (key === 'raw_json') {
          value = JSON.stringify(this.highlightNestedObject(value, this.filters), null, 2);
        } else {
          for (const key in value) {
            if (typeof value[key] === 'string') {
              for (const filterKey in this.filters) {
                if (this.filters[filterKey]) {
                  value[key] = this.highlightText(value[key], this.filters[filterKey]);
                }
              }
            }
          }
          value = JSON.stringify(value, null, 2);
        }
      }
      return value;
    },
    highlightNestedObject(obj, filters) {
      console.log("highlightNestedObject", obj, filters);
      const highlightedObj = {};
      for (const key in obj) {
        if (typeof obj[key] === 'string') {
          highlightedObj[key] = obj[key];
          for (const filterKey in filters) {
            if (filters[filterKey]) {
              highlightedObj[key] = this.highlightText(highlightedObj[key], filters[filterKey]);
            }
          }
        } else if (typeof obj[key] === 'object' && obj[key] !== null) {
          highlightedObj[key] = this.highlightNestedObject(obj[key], filters);
        } else {
          highlightedObj[key] = obj[key];
        }
      }
      return highlightedObj;
    }
  },
  computed: {
    highlightedResults() {
      return this.results.map(result => {
        const highlightedResult = {};
        for (const key in result) {
          highlightedResult[key] = this.formatValue(result[key], key);
        }
        return highlightedResult;
      });
    }
  }
};
</script>

<style>
.highlight {
  background-color: yellow;
}
</style>
