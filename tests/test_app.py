from fastapi.testclient import TestClient

from src.app import app


def test_unregister_participant():
    client = TestClient(app)

    response = client.delete(
        "/activities/Chess Club/participants/michael@mergington.edu"
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Removed michael@mergington.edu from Chess Club"

    activities = client.get("/activities").json()
    assert "michael@mergington.edu" not in activities["Chess Club"]["participants"]


def test_unregister_missing_participant():
    client = TestClient(app)

    response = client.delete(
        "/activities/Chess Club/participants/not-a-member@example.com"
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found"
