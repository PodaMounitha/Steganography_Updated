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
  // Normalize path separators and extract the base filename
  const name = filename.replace(/\\/g, '/').split('/').pop();
  return `${API_BASE_URL}/download/${encodeURIComponent(name)}`;
};

export default api;