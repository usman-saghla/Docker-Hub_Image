"""Tests for the small Flask example application.

These tests use Flask's built-in test client which lets you call
endpoints without starting a real HTTP server.
"""

from app import app


def test_home():
    """GET / should return the welcome message as plain text."""
    client = app.test_client()
    resp = client.get("/")

    assert resp.status_code == 200
    # Use get_data(as_text=True) so it's easy to read and compare
    assert resp.get_data(as_text=True).strip() == "Hello, World!"


def test_health():
    """GET /health should return a JSON status object."""
    client = app.test_client()
    resp = client.get("/health")

    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}