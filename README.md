# Task Management API 🚀

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Ready-blue)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![Render](https://img.shields.io/badge/Deployed-Render-black)

> A production-ready RESTful Task Management API with JWT Authentication & Docker.

**🔗 Live Demo:** https://task-management-api-dpeb.onrender.com/docs
**📦 GitHub:** https://github.com/darshanbca2026/Task-Management-API

## ✨ Features
- 🔐 JWT Authentication - Secure login/register
- ✅ Full CRUD for Tasks with user isolation
- 👤 User Management
- 🧪 Unit Testing with Pytest
- 🐳 Docker Ready
- 🗄️ PostgreSQL + SQLAlchemy

## 🛠️ Tech Stack
- **Backend:** FastAPI, Python 3.10+
- **Database:** PostgreSQL, SQLAlchemy
- **Auth:** JWT, Passlib Bcrypt
- **DevOps:** Docker, Render

## 📡 API Endpoints

| Method | Endpoint | Auth | Description |
| :--- | :--- | :---: | :--- |
| POST | /register | ❌ | Register new user |
| POST | /login | ❌ | Login & get token |
| GET | /users/me | ✅ | Get profile |
| POST | /tasks/ | ✅ | Create task |
| GET | /tasks/ | ✅ | Get all tasks |
| GET | /tasks/{id} | ✅ | Get task by ID |
| PUT | /tasks/{id} | ✅ | Update task |
| DELETE | /tasks/{id} | ✅ | Delete task |

## ⚙️ How to Run Locally
```bash
git clone https://github.com/darshanbca2026/Task-Management-API.git
cd Task-Management-API
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
Open: 127.0.0.1:8000
🐳 Run with Docker
docker-compose up --build
Run Tests
pytest -v
Author
Darshan B - BCA 2026GitHub: @darshanbca2026 LinkedIn:https://www.linkedin.com/in/b-darshan-a628192ba
