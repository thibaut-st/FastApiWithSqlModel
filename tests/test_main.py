from http import HTTPStatus

from starlette.testclient import TestClient

from src.main import app


def test_read_items() -> None:
    """Test read items."""
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == HTTPStatus.OK
        assert response.json() == {"message": "Hello World"}
