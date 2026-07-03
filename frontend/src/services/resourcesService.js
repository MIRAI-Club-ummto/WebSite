import api from './api';

export const getResources = (categorie = null) => {
  const params = categorie ? { categorie } : {};
  return api.get('/resources/', { params });
};
