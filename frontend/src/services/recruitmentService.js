import api from './api';

export const getRecruitmentStatus = () => {
  return api.get('/recruitment/settings/');
};

export const submitCandidature = (data) => {
  return api.post('/recruitment/candidatures/', data);
};
