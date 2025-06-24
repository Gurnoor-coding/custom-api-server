from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user_api():
	response = client.post("/users/", json={"name": "Diana", "email": "diana@example.com"})
	assert response.status_code == 200
	assert response.json()["name"] == "Diana"

def test_read_user_api():
	create = client.post("/users/", json={"name": "Eve", "email": "eve@example.com"})
	uid = create.json()["id"]
	response = client.get(f"/users/{uid}")
	assert response.status_code == 200
	assert response.json()["email"] == "eve@example.com"
