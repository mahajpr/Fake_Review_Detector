# Fake_Review_Detector
# 🕵️ Fake Review Detection & Explanation Tool

An AI-powered system that detects suspicious product reviews and explains **why** they are likely fake using rule-based detection, RAG (retrieval), and LLM explanations.

This project includes a **FastAPI backend** and **Streamlit admin dashboard**.

---

## 🚀 Features

* Detect fake vs genuine reviews
* Confidence score
* Explainable AI output
* Retrieval-Augmented Generation (RAG)
* Stores reviews in SQLite database
* Admin dashboard for monitoring
* Works across all e-commerce platforms

---

## 🧠 Architecture

```
User → Streamlit UI → FastAPI → Detection → RAG → LLM Explanation → Database
```

---

## 📁 Project Structure

```
backend/
│
├── database/
│   ├── db.py          # DB connection
│   └── deps.py        # dependency injection
│
├── models/
│   ├── pydantic.py    # API schemas
│   └── tables.py      # SQLAlchemy tables
│
├── reviews/
│   └── historical_review.txt   # RAG knowledge base
│
├── routes/
│   └── routes.py      # API endpoints
│
├── services/
│   ├── data.py        # fake review detection logic
│   ├── rag.py         # retrieval + FAISS
│   └── explain.py     # LLM explanation
│
├── database.db        # SQLite database
└── main.py            # FastAPI entry point
```

---

## 🛠️ Tech Stack

* FastAPI
* Streamlit
* SQLAlchemy
* SQLite
* FAISS
* Sentence Transformers
* Groq LLM API
* Python

---

## ⚙️ Setup Instructions

### 1. Clone repository

```bash
git clone https://github.com/YOUR_USERNAME/fake-review-detector.git
cd fake-review-detector
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn streamlit sqlalchemy sentence-transformers faiss-cpu groq
```

---

## 🔑 Environment Variable

Create `.env` file in backend folder:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run Backend

```bash
cd backend
uvicorn main:app --reload
```

Backend URL:

```
http://localhost:8000
```

---

## ▶️ Run Frontend

```bash
cd frontend
streamlit run app.py
```

---

## 📡 API Endpoints

### Analyze Review

```
POST /analyze
```

**Request**

```json
{
  "review": "Received this product for free in exchange for review"
}
```

**Response**

```json
{
  "prediction": "Fake",
  "confidence": 0.85,
  "explanation": "...",
  "suspicious_phrases": ["free", "exchange"],
  "similar_reviews": [...]
}
```

---

### Get all reviews

```
GET /reviews
```

### Get flagged reviews

```
GET /flagged
```

---

## 🧠 How it Works

1. User submits review
2. Detection engine checks suspicious patterns
3. RAG retrieves similar historical reviews
4. LLM explains why review looks fake
5. Results stored in database
6. Dashboard displays analytics

---

## 📊 Dataset

Uses:

* Custom historical reviews
* User-provided reviews

---

## 🔒 Ethics

* Does not scrape e-commerce sites
* Focuses on explainable AI

---
