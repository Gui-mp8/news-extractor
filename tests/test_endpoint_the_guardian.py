import pytest
from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)

def test_all_content_data():
    response = client.get("/content")
    assert response.status_code == 200

def test_filter_by_keyword():
    response = client.get("/content/keyword=pandas")
    assert response.status_code == 200

