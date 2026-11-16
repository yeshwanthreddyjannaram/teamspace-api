# TeamSpace API

A team collaboration and task management REST API built using **FastAPI, PostgreSQL, and SQLAlchemy**.

## Features

- User registration and password hashing using Argon2
- JWT-based authentication
- Protected API endpoints
- Role-Based Access Control (RBAC)
- Admin, Manager, and Member roles
- Project creation and management
- Task creation, updating, and deletion
- Task assignment to users
- Task status and due-date management
- SQLAlchemy model relationships
- Nested API responses
- Automated API testing using Pytest

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Alembic
- JWT (PyJWT)
- Argon2
- Pytest

## Project Structure

```text
TEAMSPACE/
├── app/
│   ├── routes/
│   │   ├── auth.py
│   │   ├── projects.py
│   │   └── tasks.py
│   ├── __init__.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── security.py
├── tests/
│   └── test_main.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/yeshwanthreddyjannaram/teamspace-api.git
cd teamspace-api
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql+psycopg2://username:password@localhost:5432/teamspace_db
SECRET_KEY=your_strong_secret_key
```

Replace the database credentials and secret with your own local values.

### 5. Run the application

```bash
uvicorn app.main:app --reload
```

## API Documentation

After starting the server, open:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Automated Testing

Run the test suite:

```bash
python -m pytest -v
```

Current test result: **11 tests passed**.

## Authentication

The API uses JWT Bearer tokens.

1. Register a user.
2. Log in to receive an access token.
3. Authorize through Swagger UI.
4. Access protected endpoints based on your role.

## Future Improvements

- Docker and Docker Compose
- Cloud deployment
- Additional automated test coverage
- Production-ready database migrations