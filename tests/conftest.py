from fastapi.testclient import TestClient
from main import app
client = TestClient(app)
import pytest
@pytest.fixture
def auth_headers():
    login_response = client.post(
        "/login",
        data={
            "username": "darshan",
            "password": "1qaz2wsx"
        }
    )

    assert login_response.status_code == 200

    token = login_response.json()["access_token"]

    return {
        "Authorization": f"Bearer {token}"
    }

@pytest.fixture
def task(auth_headers):

    response = client.post(
        "/tasks",
        json={
            "title": "Test Task",
            "description": "Test description"
        },
        headers=auth_headers
    )

    assert response.status_code in [200, 201]

    return response.json()