"""Basic app tests."""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_landing_page_loads():
    """Landing page returns 200."""
    response = client.get("/")
    assert response.status_code == 200
    assert "Zid SDK Demo" in response.text
