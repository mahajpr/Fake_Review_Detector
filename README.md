# 🧠 Fake Review Detector

## 📌 Overview

The **Fake Review Detector** is an AI-powered application designed to identify whether a product review is genuine or fake.

This project helps improve trust in online platforms by detecting misleading or spam reviews.


---

## 🚀 Features

* 🔍 Detects fake vs genuine reviews
* ⚡ FastAPI backend for efficient API handling
* 🎯 Machine Learning model for classification
* 💻 Interactive UI (Streamlit) for user input
* 📊 Real-time prediction results

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Backend:** FastAPI
* **Frontend:** Streamlit
* **Database:** SQLite (if used)
* Concepts:RAG

---

## 📂 Project Structure

```
Fake_Review_detector/
│
├── backend/                  # FastAPI backend
│   ├── __pycache__/          # Python cache files
│   ├── database/             # Database connection & config
│   ├── models/               # ML model files
│   ├── reviews/              # Review data handling
│   ├── routes/               # API routes/endpoints
│   ├── services/             # Business logic
│   ├── database.db           # SQLite database
│   ├── main.py               # FastAPI entry point
│   ├── requirements.txt      # Backend dependencies
│   └── Dockerfile            # Backend container config
│
├── frontend/                 # Streamlit frontend
│   ├── app.py                # UI application
│   ├── requirements.txt      # Frontend dependencies
│   └── Dockerfile            # Frontend container config
│
├── .env                      # Environment variables
├── .env.example              # Sample env file
├── .gitignore                # Git ignore rules
├── docker-compose.yml        # Multi-container setup
└── README.md                 # Project documentation
```

```

## ⚙️ Installation

git clone https://github.com/your-username/fake-review-detector.git
cd fake-review-detector
pip install -r requirements.txt
```

---

## ▶️ How to Run

### 1️⃣ Start Backend (FastAPI)

```bash
uvicorn main:app --reload
```

### 2️⃣ Start Frontend (Streamlit)

```bash
streamlit run app.py
```

---

## 🧪 Example Usage

1. Enter a customer review in the input box
2. Click on **Analyze Review**
3. The system predicts whether the review is **Fake** or **Genuine**

---

## 📸 Screenshots

<img width="1277" height="579" alt="Screenshot 2026-04-09 001302" src="https://github.com/user-attachments/assets/852e5163-ca5b-475b-b7a0-526f89e56bb9" />

---

## 💡 Use Cases

* 🛒 E-commerce platforms (Amazon, Flipkart)
* ⭐ Product review analysis
* 🚫 Spam detection systems
* 📊 Business intelligence tools

---


## 👩‍💻 Author

**Maha Vigneshwari**
Generative AI Developer

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to contribute!
