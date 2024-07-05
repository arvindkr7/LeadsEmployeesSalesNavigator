export function highlightText(data, filters) {
    const highlightedData = [];
  
    // Check if filters is null or empty object
    if (!filters || Object.keys(filters).length === 0) {
      // Return original data without highlighting
      return data;
    }
  
    // Iterate through each item in data
    data.forEach(item => {
      const highlightedItem = {};
  
      // Iterate through each key in filters
      for (const key in filters) {
        if (Object.hasOwnProperty.call(filters, key)) {
          const filterValue = filters[key];
  
          // Ensure filterValue is a string before applying toLowerCase
          const filterString = filterValue ? filterValue.toString().toLowerCase() : '';

          // Handle item[key] being null or undefined
          const itemValue = item[key] ? item[key].toString().toLowerCase() : '';
  
          // Check if item value contains filter value
          if (itemValue.includes(filterString)) {
            highlightedItem[key] = `<span class="highlight">${item[key]}</span>`;
          } else {
            highlightedItem[key] = item[key];
          }
        } else {
          // If filter is not defined, just assign item's value
          highlightedItem[key] = item[key];
        }
      }
  
      highlightedData.push(highlightedItem);
    });
  
    return highlightedData;
  }
