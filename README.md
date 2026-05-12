# Auth & Authorization Service — FastAPI

A production-ready authentication and authorization backend built with FastAPI, PostgreSQL, and JWT tokens. Designed with a clean layered architecture and real-world security practices.

---

## Features

- User registration with strong password validation
- JWT access tokens + refresh tokens
- Refresh token stored in DB and validated on use
- Token type enforcement (access vs refresh tokens are separate)
- Secure logout (refresh token invalidated in DB)
- Role-based user model (`user` / `admin`)
- Protected routes via OAuth2 Bearer scheme
- CORS middleware configured
- Pydantic v2 request/response validation
- SQLAlchemy 2.x ORM with PostgreSQL

---

## Project Structure

```
app/
├── main.py               # App entry point, lifespan, CORS
├── api/
│   ├── auth.py           # Route handlers
│   └── deps.py           # Dependency injection (get_db, get_current_user)
├── core/
│   ├── config.py         # Settings from .env
│   └── security.py       # Hashing, JWT create/verify
├── db/
│   └── database.py       # SQLAlchemy engine + session
├── models/
│   └── user.py           # User ORM model
├── schemas/
│   └── user_schema.py    # Pydantic schemas
├── services/
│   └── auth_service.py   # Business logic
└── utils/
    └── helpers.py
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy 2.x |
| Validation | Pydantic v2 |
| Password Hashing | passlib (bcrypt) |
| JWT | python-jose |
| Server | Uvicorn |

---

## Setup & Installation

```bash
git clone https://github.com/VarunSuddala/Auth-Authorization-Service-fastapi.git
cd Auth-Authorization-Service-fastapi

# Create and activate virtual environment
python -m venv venv

# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://postgres:yourpassword@localhost/authdb
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7
```

---

## Run the Server

```bash
uvicorn app.main:app --reload
```

Interactive API docs available at `http://127.0.0.1:8000/docs`

---

## API Endpoints

### `POST /auth/register`

Register a new user.

**Request:**
```json
{
  "full_name": "Varun Suddala",
  "email": "varun@example.com",
  "password": "Secure@123"
}
```

Password rules: min 8 characters, must include uppercase, lowercase, number, and special character (`!@#$%^&*`).

**Response `201`:**
```json
{
  "id": 1,
  "full_name": "Varun Suddala",
  "email": "varun@example.com",
  "role": "user"
}
```

---

### `POST /auth/login`

Login with email and password (OAuth2 form).

**Form fields:** `username` (email), `password`

**Response `200`:**
```json
{
  "access_token": "<jwt>",
  "refresh_token": "<jwt>",
  "token_type": "bearer"
}
```

---

### `GET /auth/me`

Get current authenticated user. Requires `Authorization: Bearer <access_token>` header.

**Response `200`:**
```json
{
  "id": 1,
  "full_name": "Varun Suddala",
  "email": "varun@example.com",
  "role": "user"
}
```

---

### `POST /auth/refresh`

Get a new access token using a valid refresh token.

**Request body:**
```json
{
  "refresh_token": "<jwt>"
}
```

**Response `200`:**
```json
{
  "access_token": "<new_jwt>",
  "refresh_token": "<same_refresh_jwt>",
  "token_type": "bearer"
}
```

---

### `POST /auth/logout`

Logout the current user. Invalidates the refresh token in the database. Requires `Authorization: Bearer <access_token>` header.

**Response `200`:**
```json
{
  "message": "Logout success"
}
```

---

## Security Design

- Passwords hashed with bcrypt, plain text never stored
- Access tokens expire in 30 minutes (configurable)
- Refresh tokens expire in 7 days (configurable)
- Token `type` field enforced — refresh tokens cannot be used as access tokens
- Refresh token validated against DB on every use — invalidated at logout
- All secrets loaded from environment variables, never hardcoded

---

## Roadmap

- [ ] Alembic database migrations
- [ ] Email verification on registration
- [ ] Password reset flow
- [ ] Role-Based Access Control (RBAC) — admin routes
- [ ] Redis for token blacklisting
- [ ] Rate limiting
- [ ] Docker + docker-compose setup
- [ ] CI/CD pipeline
- [ ] OAuth2 social login (Google)

---

## Author

**Varun Suddala**  
[GitHub](https://github.com/VarunSuddala)
