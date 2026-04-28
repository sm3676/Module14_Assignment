# Module 14: BREAD Functionality for Calculations

## 📌 Project Overview
This project implements full **BREAD (Browse, Read, Edit, Add, Delete)** functionality for calculations using **FastAPI**, with frontend integration, testing, and CI/CD.

---

## 🚀 Features

### 🔐 Authentication
- User Registration
- User Login (JWT आधारित authentication)
- Secure password hashing

### 🧮 Calculations (BREAD)
- ➕ Add Calculation
- 📥 Browse All Calculations
- 🔍 Read Single Calculation
- ✏️ Edit Calculation
- ❌ Delete Calculation

---

## 🛠️ Tech Stack
- Python (FastAPI)
- SQLite / PostgreSQL
- Pydantic
- JWT Authentication
- Playwright (E2E Testing)
- Pytest
- Docker
- GitHub Actions (CI/CD)

---

## 📂 Project Structure

backend-assignment/
│
├── app/
│ ├── main.py
│ ├── models.py
│ ├── database.py
│ ├── Auth.py
│ └── routes/
│ ├── user.py
│ └── calculation.py
│
├── module13-fastapi-jwt/
│ └── Frontend/
│ ├── index.html
│ ├── login.html
│ ├── register.html
│ └── script.js
│
├── tests/
│ ├── test_users.py
│ ├── test_calculations.py
│ └── test_e2e.py
│
├── requirements.txt
├── Dockerfile
└── README.md


---

## ▶️ How to Run Locally

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt

2️⃣ Run FastAPI server

uvicorn app.main:app --reload

Open in browser:

http://127.0.0.1:8000/docs

🧪 Run Tests

pytest

🌐 Frontend Usage

Open:

register.html → Register user
login.html → Login & get token
index.html → Perform calculations


🐳 Docker

Build image

docker build -t module14-bread-calculations .

Run container

docker run -p 8000:8000 module14-bread-calculations

⚙️ GitHub Actions (CI/CD)

Automatically runs tests on push
Builds project
Ensures everything works before submission




