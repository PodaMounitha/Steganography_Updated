import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000';

const api = axios.create({
  baseURL: API_BASE_URL,
});

export const hideFile = async (image, file, password) => {
  const formData = new FormData();
  formData.append('image', image);
  formData.append('file', file);
  formData.append('password', password);

  const response = await api.post('/hide-file', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
  return response.data;
};

export const extractFile = async (image, password) => {
  const formData = new FormData();
  formData.append('image', image);
  formData.append('password', password);

  const response = await api.post('/extract-file', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
    responseType: 'blob', // Important for downloading files
  });
  return response.data;
};

export const getDownloadUrl = (filename) => {
  // Extract filename from "outputs/hidden.png" if necessary
  const name = filename.split('/').pop() || filename.split('\\').pop();
  return `${API_BASE_URL}/download/${name}`;
};

export default api;