# tests/test_app.py
from app import app

def test_home_status_code():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200

def test_home_content():
    tester = app.test_client()
    response = tester.get('/')
    assert b"Hello from CI/CD pipeline!" in response.data

def test_content_type():
    tester = app.test_client()
    response = tester.get('/')
    assert response.content_type == "text/html; charset=utf-8"
