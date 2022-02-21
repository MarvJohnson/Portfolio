import axios from 'axios';

const BASE_URL =
  process.env.VUE_APP_MODE === 'dev'
    ? 'http://localhost:8000/'
    : `https://mj-portfolio-back-end.herokuapp.com/`;

const Client = axios.create({
  baseURL: BASE_URL
});

export default Client;
