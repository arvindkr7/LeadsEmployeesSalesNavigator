import axios from 'axios';

// Base URL for your API
const BASE_URL = 'http://localhost:8000/api';

// Function to make API calls
export const apiCall = async (endpoint, params = {}, method = 'post') => {
  console.log('endpoint', endpoint);
  try {
    const response = await axios({
      method: method,
      url: `${BASE_URL}${endpoint}`,
      data: params,
      withCredentials: true, // Include credentials if needed
      headers: {
        'Content-Type': 'application/json',
      },
    });
    return response.data;
  } catch (error) {
    console.error('API call error:', error);
    throw error;
  }
};
