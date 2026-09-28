import { useEffect, useState } from "react";

function App() {
  const [status, setStatus] = useState("prüfe …");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/health")
      .then((res) => res.json())
      .then((data) =>
        setStatus(data.status === "ok" ? "Backend erreichbar ✅" : "Unerwartete Antwort")
      )
      .catch(() => setStatus("Backend nicht erreichbar ❌"));
  }, []);

  return (
    <main style={{ fontFamily: "sans-serif", padding: 40 }}>
      <h1>OSINT-Plattform</h1>
      <p>{status}</p>
    </main>
  );
}

export default App;