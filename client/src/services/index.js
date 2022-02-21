import axios from 'axios';

const BASE_URL =
  process.env.VUE_APP_MODE === 'prod'
    ? `${window.location.origin}/api/v1/`
    : 'http://localhost:8000/';

const Client = axios.create({
  baseURL: BASE_URL
});

export default Client;
