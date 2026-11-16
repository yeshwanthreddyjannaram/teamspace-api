# TeamSpace API

A REST API for team collaboration and task management, built with **Python, FastAPI, and PostgreSQL**.

TeamSpace allows users to manage projects, create and assign tasks, track task progress, and access resources according to their roles.

## Live Deployment

- **API Base URL:** https://teamspace-api-llgv.onrender.com
- **Interactive API Documentation:** https://teamspace-api-llgv.onrender.com/docs
- **GitHub Repository:** https://github.com/yeshwanthreddyjannaram/teamspace-api

## Features

- User registration with Argon2 password hashing
- User login with JWT authentication
- Protected API endpoints
- Role-Based Access Control (RBAC):
  - Admin
  - Manager
  - Member
- Project creation, retrieval, updating, and deletion
- Task creation, retrieval, updating, and deletion
- Task assignment to users
- Task status management
- Task due-date management
- SQLAlchemy model relationships
- Nested API responses
- Automated testing with Pytest
- Docker and Docker Compose support
- Cloud deployment with Render and Neon PostgreSQL

## Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Programming language |
| FastAPI | REST API framework |
| PostgreSQL | Relational database |
| SQLAlchemy | ORM |
| Pydantic | Data validation |
| PyJWT | JWT authentication |
| pwdlib (Argon2) | Password hashing |
| Pytest | Automated testing |
| Docker | Containerization |
| Docker Compose | Multi-container setup |
| Render | API deployment |
| Neon | Hosted PostgreSQL database |

## Project Structure

```text
TEAMSPACE/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── security.py
│   │
│   └── routes/
│       ├── __init__.py
│       ├── auth.py
│       ├── projects.py
│       └── tasks.py
│
├── tests/
│   └── test_main.py
│
├── .env
├── .gitignore
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/yeshwanthreddyjannaram/teamspace-api.git
cd teamspace-api
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a PostgreSQL database

Create a database named `teamspace_db` using PostgreSQL or pgAdmin.

Alternatively, run this SQL command:

```sql
CREATE DATABASE teamspace_db;
```

### 5. Configure environment variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql+psycopg2://username:password@localhost:5432/teamspace_db
SECRET_KEY=your-secret-key
```

Replace the database username and password with your local PostgreSQL credentials. Use a strong, randomly generated secret key.

Never commit your `.env` file to GitHub.

### 6. Start the application

```bash
uvicorn app.main:app --reload
```

The API will be available at:

- API: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Run with Docker

Make sure Docker Desktop is running.

### 1. Configure environment variables

Create a `.env` file in the project root containing:

```env
SECRET_KEY=your-secret-key
```

The Docker Compose configuration supplies the database connection URL to the API container.

### 2. Build and start containers

```bash
docker compose up --build -d
```

### 3. Access the API

- API: http://localhost:8000
- Swagger UI: http://localhost:8000/docs

### 4. Stop containers

```bash
docker compose down
```

To remove the database volume and its stored data:

```bash
docker compose down -v
```

**Note:** The PostgreSQL credentials in the provided Docker Compose configuration are for local development only. Do not use them in production.

## Authentication

TeamSpace uses JWT-based authentication.

1. Register a user through `/auth/`.
2. Log in through `/auth/login`.
3. Receive a JWT access token.
4. Use the token to access protected endpoints.
5. The API identifies the authenticated user and checks their permissions.

Protected endpoints require a valid access token.

## Role-Based Access Control

The API uses three roles:

| Role | Access |
|---|---|
| Admin | Administrative operations |
| Manager | Manager-level operations |
| Member | Standard project and task operations |

Access is controlled through role-based authorization checks.

## API Modules

| Module | Functionality |
|---|---|
| `/auth/` | User registration |
| `/auth/login` | User login and JWT generation |
| `/auth/me` | Retrieve authenticated user details |
| `/projects/` | Project management |
| `/tasks/` | Task management |

For request bodies, response formats, and available operations, refer to the interactive Swagger documentation.

## Automated Testing

The project uses Pytest and FastAPI's TestClient for automated API testing.

Run the test suite:

```bash
python -m pytest -v
```

**Test result:** 11 tests passed.

The tests cover registration, duplicate registration, login, authentication, invalid tokens, and role-based access control.

## Deployment

The application is deployed using:

- **Render:** Hosts the FastAPI application.
- **Neon:** Provides the hosted PostgreSQL database.
- **Docker:** Packages the application for deployment.

Live API: https://teamspace-api-llgv.onrender.com

Swagger documentation: https://teamspace-api-llgv.onrender.com/docs

## Future Improvements

- Add and maintain database schema migrations.
- Expand automated test coverage.
- Improve production logging and error handling.
- Add pagination and filtering for larger datasets.
- Add frontend integration.

---

**Author:** Yeshwanth Reddy Jannaram

**GitHub:** https://github.com/yeshwanthreddyjannaram