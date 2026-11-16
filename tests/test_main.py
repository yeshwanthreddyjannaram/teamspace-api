
from fastapi.testclient import TestClient
from app.main import app
import uuid 
from app.database import SessionLocal
from app import models

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_register_user():
    email = f"test_{uuid.uuid4().hex[:8]}@example.com"

    response = client.post(
        "/auth/",
        json={
            "name": "Test User",
            "email": email,
            "password": "TestPassword123"
        }
    )

    assert response.status_code == 201
    assert response.json()["email"] == email


def test_duplicate_email():
    response = client.post(
        "/auth/",
        json={
            "name": "Test User",
            "email": "pytest_user4@example.com",
            "password": "TestPassword123"
        }
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Email is already registered"


def test_login_user():
    response = client.post(
        "/auth/login",
        data={
            "username": "pytest_user3@example.com",
            "password": "TestPassword123"
        }
    )

    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"



def test_get_current_user():
    login_response = client.post(
        "/auth/login",
        data={
            "username": "pytest_user3@example.com",
            "password": "TestPassword123"
        }
    )

    token = login_response.json()["access_token"]

    response = client.get(
        "/auth/me",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200
    assert response.json()["email"] == "pytest_user3@example.com"
    
    
def test_get_current_user_unauthorized():
    response = client.get("/auth/me")

    assert response.status_code == 401
    
def test_invalid_token():
    response = client.get(
        "/auth/me",
        headers={
            "Authorization": "Bearer invalid_token_123"
        }
    )

    assert response.status_code == 401
    

def test_member_cannot_access_admin_route():
    login_response = client.post(
        "/auth/login",
        data={
            "username": "pytest_user3@example.com",
            "password": "TestPassword123"
        }
    )

    token = login_response.json()["access_token"]

    response = client.get(
        "/auth/admin-test",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 403
    



def test_admin_can_access_admin_route():
    db = SessionLocal()

    user = db.query(models.User).filter(
        models.User.email == "pytest_user3@example.com"
    ).first()

    original_role = user.role
    user.role = "admin"
    db.commit()

    try:
        login_response = client.post(
            "/auth/login",
            data={
                "username": "pytest_user3@example.com",
                "password": "TestPassword123"
            }
        )

        token = login_response.json()["access_token"]

        response = client.get(
            "/auth/admin-test",
            headers={
                "Authorization": f"Bearer {token}"
            }
        )

        assert response.status_code == 200

    finally:
        user.role = original_role
        db.commit()
        db.close()


def test_member_cannot_access_manager_route():
    login_response = client.post(
        "/auth/login",
        data={
            "username": "pytest_user3@example.com",
            "password": "TestPassword123"
        }
    )

    token = login_response.json()["access_token"]

    response = client.get(
        "/auth/manager-test",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 403


def test_manager_can_access_manager_route():
    db = SessionLocal()

    user = db.query(models.User).filter(
        models.User.email == "pytest_user3@example.com"
    ).first()

    original_role = user.role
    user.role = "manager"
    db.commit()

    try:
        login_response = client.post(
            "/auth/login",
            data={
                "username": "pytest_user3@example.com",
                "password": "TestPassword123"
            }
        )

        token = login_response.json()["access_token"]

        response = client.get(
            "/auth/manager-test",
            headers={
                "Authorization": f"Bearer {token}"
            }
        )

        assert response.status_code == 200

    finally:
        user.role = original_role
        db.commit()
        db.close()


