from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_posts():
    response = client.get("/posts/")
    assert response.status_code == 200
    assert response.json() == []

def test_create_post():
    response = client.post("/posts/", json={"title": "Test Post", "content": "Test Content"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Post"
    assert data["content"] == "Test Content"
    assert "id" in data

    # 추가로 생성된 게시글 목록 확인
    response = client.get("/posts/")
    assert response.status_code == 200
    posts = response.json()
    assert len(posts) == 1
    assert posts[0]["title"] == "Test Post"