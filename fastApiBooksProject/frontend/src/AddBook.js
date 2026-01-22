import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Routes, Route, useNavigate } from "react-router-dom";

function Home() {
  const [books, setBooks] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    fetch("http://127.0.0.1:8000/getAllBooks")
      .then((res) => res.json())
      .then((data) => setBooks(data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Library Dashboard</h1>

      <button className="btn btn-primary" onClick={() => navigate("/add-book")}>
        Add New Book
      </button>

      <div style={{ marginTop: "20px" }}>
        {books.map((book, index) => (
          <div key={index} style={{ border: "1px solid #ddd", padding: "10px", marginBottom: "10px", width: "300px" }}>
            <h3>{book.name}</h3>
            <p><strong>Author:</strong> {book.author}</p>
            <p><strong>Rating:</strong> ⭐ {book.rating}</p>
            <p><strong>Published:</strong> {book.published_year}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

function AddBook() {
  const navigate = useNavigate();

  const [form, setForm] = useState({
    name: "",
    author: "",
    published_year: "",
    rating: "",
  });

  const handleSubmit = async (e) => {
    e.preventDefault();

    const response = await fetch("http://127.0.0.1:8000/createBook", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form),
    });

    if (response.ok) {
      alert("Book added successfully!");
      navigate("/"); // go back to home page
    } else {
      alert("Failed to add book");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Add New Book</h2>

      <form onSubmit={handleSubmit} style={{ width: "300px" }}>
        <label>Name:</label>
        <input
          className="form-control"
          value={form.name}
          onChange={(e) => setForm({ ...form, name: e.target.value })}
          required
        />

        <label>Author:</label>
        <input
          className="form-control"
          value={form.author}
          onChange={(e) => setForm({ ...form, author: e.target.value })}
          required
        />

        <label>Published Year:</label>
        <input
          className="form-control"
          value={form.published_year}
          onChange={(e) => setForm({ ...form, published_year: e.target.value })}
          required
        />

        <label>Rating:</label>
        <input
          className="form-control"
          value={form.rating}
          onChange={(e) => setForm({ ...form, rating: e.target.value })}
          required
        />

        <button type="submit" className="btn btn-success" style={{ marginTop: "10px" }}>
          Submit
        </button>
      </form>
    </div>
  );
}

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
