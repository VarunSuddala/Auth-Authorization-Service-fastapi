# Auth & Authorization Service (FastAPI)

A production-grade authentication and authorization backend built with FastAPI.
Designed with scalable architecture, security best practices, and real-world backend patterns.

---

## Features

### Implemented (Day 1)

* User Registration API
* Password Hashing using bcrypt (via passlib)
* PostgreSQL Database Integration
* SQLAlchemy ORM
* Pydantic v2 Validation
* Clean Modular Architecture (Controller → Service → DB)

###  Upcoming (Roadmap)

* JWT Authentication (Access + Refresh Tokens)
* Role-Based Access Control (RBAC)
* Email Verification System
* Password Reset Flow
* Token Blacklisting / Logout
* Audit Logging
* Docker Deployment

---

##  Architecture

```
API Layer → Service Layer → Database Layer → Security Layer
```

###  Project Structure

```
auth_service/
│
├── app/
│   ├── main.py
│   ├── core/          # config, security
│   ├── db/            # database connection
│   ├── models/        # SQLAlchemy models
│   ├── schemas/       # Pydantic schemas
│   ├── api/           # routes/controllers
│   ├── services/      # business logic
│   ├── utils/         # helpers
│
├── .env
├── requirements.txt
├── README.md
```

---

##  Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy
* Pydantic v2
* Passlib (bcrypt)
* python-jose (JWT - upcoming)

---

## Setup & Installation

```bash
git clone https://github.com/VarunSuddala/Auth-Authorization-Service-fastapi.git
cd Auth-Authorization-Service-fastapi

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

---

##  Environment Variables

Create a `.env` file:

```env
DATABASE_URL=postgresql://postgres:yourpassword@localhost/authdb
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

##  Run the Server

```bash
uvicorn app.main:app --reload
```

---

##  API Documentation

FastAPI provides built-in interactive docs:

```
http://127.0.0.1:8000/docs
```

---

##  API Endpoints

###  POST `/auth/register`

Registers a new user.

#### Request:

```json
{
  "full_name": "Varun",
  "email": "varun@gmail.com",
  "password": "secure123"
}
```

#### Response:

```json
{
  "id": 1,
  "full_name": "Varun",
  "email": "varun@gmail.com",
  "role": "user"
}
```

#### Error:

```json
{
  "detail": "User with this email already exists"
}
```

---

##  Security Notes

* Passwords are hashed using bcrypt before storage
* Plain text passwords are never stored
* Validation is handled at schema level using Pydantic
* Database constraints enforce uniqueness

---
---

##  Motivation

This project is part of a backend engineering roadmap focused on building real-world systems similar to authentication services used in:

* Google (Account Authentication)
* Amazon (Identity Services)
* Netflix (User Authentication Backend)

---

##  Future Improvements

* Add Redis for token blacklisting
* Add rate limiting
* Add OAuth (Google Login)
* Add CI/CD pipeline

---

##  Status

 Actively under development — evolving into a full production-ready authentication system.

---

##  Author

**Varun Suddala**

---
