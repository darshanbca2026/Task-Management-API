README.MD

# Task Management API 🚀

A secure Task Management REST API built with FastAPI - with Authentication, Testing, Mocking & Docker.

## ✨ Features
- JWT Authentication
- CRUD for Tasks (Create, Read, Update, Delete)
- User Management
- Unit Testing with Pytest & Mocking
- Docker & Docker Compose Support
- SQLite / Postgres Ready

## 🛠️ Tech Stack
- FastAPI, Python 3.10+
- SQLAlchemy
- Pytest
- Docker

## 📁 Project Structure
.
├── main.py
├── auth.py
├── crud.py
├── model.py
├── schemas.py
├── security.py
├── database.py
├── tests/
├── Dockerfile
├── docker-compose.yml
└── requirements.txt

## ⚙️ How to Run Locally
```bash
git clone https://github.com/darshanbca2026/Task-Management-API.git
cd Task-Management-API
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
 
🐳 Run with Docker 

docker-compose up --build

Run Teststpytest -v


**Step 4:** `Ctrl + S` save it

**Step 5:** type in terminal

```powershell
git add README.md
git commit -m "add complete README"
git push

