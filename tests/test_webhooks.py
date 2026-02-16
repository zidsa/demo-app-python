"""Webhook endpoint tests."""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_api_webhooks_requires_auth():
    """Webhook list endpoint requires authentication."""
    response = client.get("/api/webhooks")
    assert response.status_code == 401
