# test_app.py
from app import app  # Import your Flask app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.data == b"Hello, Docker!"
    assert response.status_code == 200
