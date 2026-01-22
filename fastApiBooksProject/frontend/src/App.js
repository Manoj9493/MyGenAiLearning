import React, { useEffect, useState } from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  useNavigate
} from "react-router-dom";

/* ------------------- HOME (Dashboard) -------------------- */

function Home() {
  const [books, setBooks] = useState([]);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    async function fetchBooks() {
      try {
        const res = await fetch("http://localhost:8000/");
        const data = await res.json();
        setBooks(data);
      } catch (err) {
        console.error("Fetch error:", err);
      }
      setLoading(false);
    }
    fetchBooks();
  }, []);

  return (
    <div className="app-root">
      <style>{`
        :root{
          --bg:#f5f7fb;
          --card:#ffffff;
          --muted:#6b7280;
          --accent:#2563eb;
          --success:#16a34a;
        }
        body,html,#root{margin:0;padding:0;font-family: Inter;}
        .site-header{
          display:flex;justify-content:space-between;align-items:center;
          padding:20px;background:white;box-shadow:0 2px 8px #00000010;
        }
        .btn{padding:10px 14px;border-radius:10px;border:0;cursor:pointer;font-weight:600;}
        .btn-primary{background:var(--accent);color:white;}
        .btn-green{background:var(--success);color:white;}
        .grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:20px;}
        .card{background:white;padding:20px;border-radius:14px;box-shadow:0 4px 12px #00000010;}
      `}</style>

      <header className="site-header">
        <h1>Library Dashboard</h1>

        <div style={{ display: "flex", gap: "12px" }}>
          <button className="btn btn-primary" onClick={() => navigate("/add-book")}>
            Add New Book
          </button>

          <button className="btn btn-green">Update Book</button>
        </div>
      </header>

      <main style={{ padding: "20px" }}>
        {loading ? (
          <p>Loading...</p>
        ) : (
          <div className="grid">
            {books.map((book) => (
              <div key={book.id} className="card">
                <h3>{book.name}</h3>
                <p><b>Author:</b> {book.author}</p>
                <p><b>Published:</b> {book.published_year}</p>
                <p><b>Rating:</b> ⭐ {book.rating}</p>
              </div>
            ))}
          </div>
        )}
      </main>
    </div>
  );
}

/* ------------------- ADD BOOK FORM -------------------- */

function AddBook() {
  const navigate = useNavigate();
  const [form, setForm] = useState({
    name: "",
    author: "",
    published_year: "",
    rating: ""
  });

  function updateField(e) {
    setForm({ ...form, [e.target.name]: e.target.value });
  }

  async function handleSubmit(e) {
    e.preventDefault();

    const res = await fetch("http://localhost:8000//books/createBook", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form)
    });

    if (res.ok) {
      alert("Book added successfully!");
      navigate("/");
    } else {
      alert("Error adding book");
    }
  }

  return (
    <div style={{ padding: 30, maxWidth: 400, margin: "auto" }}>
      <h2>Add New Book</h2>

      <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", gap: 12 }}>
        <input type="text" name="name" placeholder="Book Name" required onChange={updateField} />
        <input type="text" name="author" placeholder="Author" required onChange={updateField} />
        <input type="text" name="published_year" placeholder="Published Year" required onChange={updateField} />
        <input type="text" name="rating" placeholder="Rating" required onChange={updateField} />

        <button className="btn btn-primary" type="submit">Submit</button>
      </form>
    </div>
  );
}

/* ------------------- MAIN APP ROUTER -------------------- */

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/add-book" element={<AddBook />} />
      </Routes>
    </Router>
  );
}
