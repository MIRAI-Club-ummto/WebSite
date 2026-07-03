import React, { useEffect, useState } from 'react'
import { getResources } from '../services/resourcesService'

const CATEGORIES = [
  { value: null,           label: 'Toutes' },
  { value: 'pdf',          label: 'PDF' },
  { value: 'support_cours',label: 'Support de cours' },
  { value: 'tutoriel',     label: 'Tutoriel' },
  { value: 'presentation', label: 'Présentation' },
  { value: 'lien_utile',   label: 'Lien utile' },
]

export default function Resources() {
  const [resources, setResources] = useState([])
  const [categorie, setCategorie] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    setLoading(true)
    getResources(categorie)
      .then(res => setResources(res.data))
      .catch(() => setResources([]))
      .finally(() => setLoading(false))
  }, [categorie])

  return (
    <div style={{padding:'2rem',color:'white'}}>
      <h1>Ressources</h1>
      <div style={{display:'flex',gap:'0.5rem',margin:'1rem 0',flexWrap:'wrap'}}>
        {CATEGORIES.map(c => (
          <button key={c.label} onClick={() => setCategorie(c.value)}
            style={{padding:'0.4rem 1rem',borderRadius:'999px',cursor:'pointer',
              background: categorie === c.value ? '#A855F7' : 'transparent',
              color: categorie === c.value ? '#0D0D1A' : 'white',
              border:'1px solid #A855F7'}}>
            {c.label}
          </button>
        ))}
      </div>
      {loading ? <p>Chargement...</p> : resources.length === 0 ? <p>Aucune ressource.</p> :
        <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fill,minmax(280px,1fr))',gap:'1rem'}}>
          {resources.map(r => (
            <div key={r.id} style={{background:'rgba(255,255,255,0.05)',border:'1px solid rgba(168,85,247,0.2)',borderRadius:'10px',padding:'1.25rem'}}>
              <span style={{fontSize:'0.7rem',color:'#D4A017',textTransform:'uppercase'}}>{r.categorie_label}</span>
              <h3 style={{margin:'0.4rem 0'}}>{r.titre}</h3>
              <p style={{fontSize:'0.85rem',color:'#8080A0'}}>{r.description}</p>
              {r.fichier_url && <a href={r.fichier_url} target="_blank" rel="noreferrer" style={{color:'#A855F7',fontSize:'0.85rem'}}>Accéder →</a>}
            </div>
          ))}
        </div>
      }
    </div>
  )
}
