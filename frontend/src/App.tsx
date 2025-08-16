import React, { useEffect, useState } from "react";
import axios from "axios";

type Show = { id: string; title: string; description?: string };

export default function App() {
  const [shows, setShows] = useState<Show[]>([]);
  useEffect(() => {
    axios.get("/api/shows").then(res => setShows(res.data)).catch(() => {});
  }, []);
  return (
    <div style={{ padding: 20 }}>
      <h1>Diffusion Spectacles — MVP</h1>
      <h2>Programmation</h2>
      {shows.length === 0 ? (
        <p>Aucun spectacle (essaye d'appeler l'API)</p>
      ) : (
        <ul>
          {shows.map(s => (
            <li key={s.id}><strong>{s.title}</strong> — {s.description}</li>
          ))}
        </ul>
      )}
    </div>
  );
}