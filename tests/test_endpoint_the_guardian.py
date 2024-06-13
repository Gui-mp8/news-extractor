import pytest
from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)

def test_content():
    response = client.get("/content")
    assert response.status_code == 200

