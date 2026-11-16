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
- Docker and Docker Compose support

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
- Docker
- Docker Compose

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
├── .dockerignore
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Installation and Setup (Local)

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

## Run with Docker

### Prerequisites

- Docker Desktop installed and running
- Docker Compose available

### 1. Configure environment variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your_strong_random_secret
```

### 2. Build and start containers

```bash
docker compose up --build -d
```

This starts the FastAPI application and PostgreSQL database together.

### 3. Access the application

- API: http://localhost:8000
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### 4. Stop the containers

```bash
docker compose down
```

To remove containers and the PostgreSQL data volume:

```bash
docker compose down -v
```

**Warning:** The `-v` option permanently deletes the PostgreSQL data stored in the Docker volume.

**Note:** The database credentials in the current Docker Compose configuration are for local development only. Replace them with secure environment-based credentials before production deployment.

## API Documentation

After starting the application, access:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Automated Testing

Run the test suite:

```bash
python -m pytest -v
```

Current test result: **11 tests passed**.

## Authentication

The API uses JWT Bearer token authentication.

1. Register a user.
2. Log in to receive an access token.
3. Authorize through Swagger UI.
4. Access protected endpoints based on your role.

## Future Improvements

- Cloud deployment
- Additional automated test coverage
- Production-ready database migrations
- Improved production security and configuration