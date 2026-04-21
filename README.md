# Backend Assignment (FastAPI + SQLAlchemy)

## 🚀 Overview
This project is a backend application built using **FastAPI**.  
It provides:
- User Registration & Login
- Calculation CRUD (Create, Read, Update, Delete)
- SQLite database using SQLAlchemy
- API documentation via Swagger UI

---

## 🛠️ Tech Stack
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Pytest
- Docker

---

## 📁 Project Structure

backend-assignment/
│
├── app/
│ ├── main.py
│ ├── db/
│ ├── models/
│ ├── schemas/
│ ├── routes/
│ └── auth/
│
├── tests/
├── requirements.txt
├── Dockerfile
└── README.md


---

## ⚙️ Installation & Run (Local)

### 1. Install dependencies
```bash
pip install -r requirements.txt

### 2. Run The Server

uvicorn app.main:app --reload

### 3. open AI docs

http://localhost:8000/docs


🐳 Run with Docker
1. Build Docker image

docker build -t backend-app .

2. Run container

docker run -p 8000:8000 backend-app

3. Access API

http://localhost:8000/docs

🧪 Running Tests

pytest

📌 API Endpoints
Users
POST /users/register → Register user
POST /users/login → Login user
Calculations
GET /calculations/ → Get all calculations
POST /calculations/ → Create calculation
GET /calculations/{id} → Get one
PUT /calculations/{id} → Update
DELETE /calculations/{id} → Delete


👩‍💻 Author

Sharvani Rao


















