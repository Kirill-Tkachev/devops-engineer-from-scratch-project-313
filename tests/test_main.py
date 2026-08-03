from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_ping():
    response = client.get("/ping")

    assert response.status_code == 200
    assert response.json() == "pong"


def test_create_link():
    response = client.post(
        "/api/links",
        json={
            "original_url": "https://google.com",
            "short_name": "google",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["original_url"] == "https://google.com"
    assert data["short_name"] == "google"
    assert "id" in data
    assert "short_url" in data


def test_get_links():
    client.post(
        "/api/links",
        json={
            "original_url": "https://google.com",
            "short_name": "google",
        },
    )

    response = client.get("/api/links")

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1
    assert data[0]["short_name"] == "google"


def test_get_link():
    create_response = client.post(
        "/api/links",
        json={
            "original_url": "https://google.com",
            "short_name": "google",
        },
    )

    link_id = create_response.json()["id"]

    response = client.get(f"/api/links/{link_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == link_id
    assert data["short_name"] == "google"


def test_update_link():
    create_response = client.post(
        "/api/links",
        json={
            "original_url": "https://google.com",
            "short_name": "google",
        },
    )

    link_id = create_response.json()["id"]

    response = client.put(
        f"/api/links/{link_id}",
        json={
            "original_url": "https://yandex.ru",
            "short_name": "yandex",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == link_id
    assert data["original_url"] == "https://yandex.ru"
    assert data["short_name"] == "yandex"


def test_delete_link():
    create_response = client.post(
        "/api/links",
        json={
            "original_url": "https://google.com",
            "short_name": "google",
        },
    )

    link_id = create_response.json()["id"]

    response = client.delete(f"/api/links/{link_id}")

    assert response.status_code == 204

    response = client.get(f"/api/links/{link_id}")

    assert response.status_code == 404