import React, { useEffect, useState } from 'react'
import { getRecruitmentStatus, submitCandidature } from '../services/recruitmentService'

export default function Recruitment() {
  const [phase, setPhase] = useState(null)
  const [form, setForm] = useState({ prenom:'', nom:'', email:'', telephone:'', niveau_etude:'', departement:'', motivation:'' })
  const [success, setSuccess] = useState(false)
  const [error, setError] = useState('')

  useEffect(() => {
    getRecruitmentStatus().then(res => setPhase(res.data.phase))
  }, [])

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError('')
    try {
      await submitCandidature(form)
      setSuccess(true)
    } catch (err) {
      setError(err.response?.data?.detail || 'Erreur lors de l\'envoi.')
    }
  }

  if (!phase) return <div style={{color:'white',padding:'2rem'}}>Chargement...</div>

  if (phase === 'ferme') return (
    <div style={{color:'white',padding:'2rem'}}>
      <h1>Recrutement</h1>
      <p style={{color:'#F87171'}}>🔒 Les candidatures sont fermées.</p>
    </div>
  )

  if (phase === 'non_demarre') return (
    <div style={{color:'white',padding:'2rem'}}>
      <h1>Recrutement</h1>
      <p style={{color:'#D4A017'}}>⏳ Le recrutement n'a pas encore commencé.</p>
    </div>
  )

  if (success) return (
    <div style={{color:'white',padding:'2rem',textAlign:'center'}}>
      <h1>🎉 Candidature envoyée !</h1>
      <p>On te recontactera par email.</p>
    </div>
  )

  return (
    <div style={{padding:'2rem',color:'white'}}>
      <h1>Candidater</h1>
      {error && <p style={{color:'#F87171'}}>{error}</p>}
      <form onSubmit={handleSubmit} style={{maxWidth:'600px',display:'flex',flexDirection:'column',gap:'1rem'}}>
        {[['prenom','Prénom'],['nom','Nom'],['email','Email'],['telephone','Téléphone'],['departement','Département']].map(([field, label]) => (
          <div key={field}>
            <label style={{fontSize:'0.85rem',color:'#B0B0C8'}}>{label} *</label><br/>
            <input type="text" value={form[field]} onChange={e => setForm({...form,[field]:e.target.value})} required
              style={{width:'100%',padding:'0.6rem',background:'rgba(255,255,255,0.05)',border:'1px solid rgba(168,85,247,0.3)',borderRadius:'6px',color:'white'}}/>
          </div>
        ))}
        <div>
          <label style={{fontSize:'0.85rem',color:'#B0B0C8'}}>Niveau d'étude *</label><br/>
          <select value={form.niveau_etude} onChange={e => setForm({...form,niveau_etude:e.target.value})} required
            style={{width:'100%',padding:'0.6rem',background:'#111827',border:'1px solid rgba(168,85,247,0.3)',borderRadius:'6px',color:'white'}}>
            <option value="">— Choisir —</option>
            {['Licence 1','Licence 2','Licence 3','Master 1','Master 2','Doctorat'].map(n => <option key={n}>{n}</option>)}
          </select>
        </div>
        <div>
          <label style={{fontSize:'0.85rem',color:'#B0B0C8'}}>Motivation *</label><br/>
          <textarea value={form.motivation} onChange={e => setForm({...form,motivation:e.target.value})} required rows={5}
            style={{width:'100%',padding:'0.6rem',background:'rgba(255,255,255,0.05)',border:'1px solid rgba(168,85,247,0.3)',borderRadius:'6px',color:'white'}}/>
        </div>
        <button type="submit" style={{padding:'0.75rem',background:'#A855F7',color:'#0D0D1A',fontWeight:'700',border:'none',borderRadius:'6px',cursor:'pointer'}}>
          🎯 Soumettre ma candidature
        </button>
      </form>
    </div>
  )
}
