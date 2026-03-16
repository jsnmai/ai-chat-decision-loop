def test_health_returns_ok(client):
    """Health endpoint returns 200 and correct body."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_health_requires_no_auth(client):
    """Health endpoint is publicly accessible without authentication."""
    response = client.get("/health")
    assert response.status_code == 200
