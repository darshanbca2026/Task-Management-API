from conftest import client
import pytest
from unittest.mock import Mock
from crud import get_tasks
import model
def test_login():
    response = client.post(
        "/login",
        data={
            "username": "darshan",
            "password": "1qaz2wsx"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_wrong_password():
     response = client.post(
        "/login",
        data={
            "username": "darshan",
            "password": "wrongpassword"
        }
    )

     assert response.status_code == 401
def test_create_task_without_token():
    response = client.post(
        "/tasks",
        json={
            "title": "Test Task",
            "description": "Testing JWT"
        }
    )

    assert response.status_code == 401
def test_create_task_with_token(auth_headers):

    response = client.post(
        "/tasks",
        json={
            "title": "Test Task",
            "description": "Testing JWT with pytest"
        },
        headers=auth_headers
    )

    assert response.status_code in [200, 201]

    data = response.json()

    assert data["title"] == "Test Task"
    assert data["description"] == "Testing JWT with pytest"

def test_create_task_with_invalid_token():
    headers = {
        "Authorization": "Bearer fake_invalid_token"
    }

    response = client.post(
        "/tasks",
        json={
            "title": "Test Task",
            "description": "Testing invalid JWT"
        },
        headers=headers
    )

    assert response.status_code == 401
def test_get_tasks_with_token(auth_headers):

    response = client.get(
        "/tasks",
        headers=auth_headers
    )

    assert response.status_code == 200
def test_get_tasks_without_token():

    response = client.get("/tasks")

    assert response.status_code == 401

def test_update_task_with_token(auth_headers):

    # 1. Create a task
    create_response = client.post(
        "/tasks",
        json={
            "title": "Old Task",
            "description": "Old description"
        },
        headers=auth_headers
    )

    assert create_response.status_code in [200, 201]

    # 2. Get task ID
    task_id = create_response.json()["id"]

    # 3. Update the task
    update_response = client.put(
        f"/tasks/{task_id}",
        json={
            "title": "Updated Task",
            "description": "Updated description"
        },
        headers=auth_headers
    )

    # 4. Check result
    assert update_response.status_code == 200

    data = update_response.json()

    assert data["title"] == "Updated Task"
    assert data["description"] == "Updated description"
def test_update_task_with_token(auth_headers, task):

    task_id = task["id"]

    response = client.put(
        f"/tasks/{task_id}",
        json={
            "title": "Updated Task",
            "description": "Updated description"
        },
        headers=auth_headers
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Updated Task"
    assert data["description"] == "Updated description"
def test_update_task_without_token():

    # 1. Try to update a task without JWT
    response = client.put(
        "/tasks/1",
        json={
            "title": "Hacked Task",
            "description": "Trying without JWT"
        }
    )

    # 2. Check that access is denied
    assert response.status_code == 401
def test_delete_task_with_token(auth_headers, task):

    task_id = task["id"]

    response = client.delete(
        f"/tasks/{task_id}",
        headers=auth_headers
    )

    assert response.status_code == 200
def test_delete_task_without_token():

    response = client.delete(
        "/tasks/1"
    )

    assert response.status_code == 401
def test_get_tasks_with_mock():

    fake_db = Mock()

    fake_db.query.return_value.filter.return_value.all.return_value = [
        "Task 1",
        "Task 2"
    ]

    result = get_tasks(fake_db, user_id=1)

    assert result == ["Task 1", "Task 2"]

    fake_db.query.assert_called_once()
    fake_db.query.return_value.filter.assert_called_once()
    fake_db.query.return_value.filter.return_value.all.assert_called_once()





