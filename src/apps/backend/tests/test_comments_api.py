import pytest
from flask import Flask
from modules.comment.rest_api.comment_rest_api_server import CommentRestApiServer


@pytest.fixture
def client():
    app = Flask(__name__)
    CommentRestApiServer(app)

    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_create_comment_success(client):
    response = client.post(
        "/tasks/task123/comments",
        json={"text": "This is a test comment"}
    )

    assert response.status_code == 201
    data = response.get_json()
    assert data["text"] == "This is a test comment"
    assert data["task_id"] == "task123"


def test_create_comment_empty_text(client):
    response = client.post(
        "/tasks/task123/comments",
        json={"text": ""}
    )

    assert response.status_code == 400


def test_get_comments_for_task(client):
    client.post(
        "/tasks/task1/comments",
        json={"text": "First comment"}
    )
    client.post(
        "/tasks/task1/comments",
        json={"text": "Second comment"}
    )

    response = client.get("/tasks/task1/comments")
    data = response.get_json()

    assert response.status_code == 200
    assert len(data) == 2


def test_update_comment(client):
    create_resp = client.post(
        "/tasks/task1/comments",
        json={"text": "Old text"}
    )
    comment_id = create_resp.get_json()["id"]

    update_resp = client.put(
        f"/comments/{comment_id}",
        json={"text": "Updated text"}
    )

    assert update_resp.status_code == 200
    assert update_resp.get_json()["text"] == "Updated text"


def test_delete_comment(client):
    create_resp = client.post(
        "/tasks/task1/comments",
        json={"text": "To be deleted"}
    )
    comment_id = create_resp.get_json()["id"]

    delete_resp = client.delete(f"/comments/{comment_id}")
    assert delete_resp.status_code == 200
