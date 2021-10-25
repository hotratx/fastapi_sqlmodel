import json

from app.api.crud.songs import SongDB
from app.api.models.models import Song, SongCreate


def test_post_song(test_app, monkeypatch):
    test_request_payload = {'name': 'amim', 'artist': 'eu', 'year': 19}

    async def mock_post(db, session):
        return test_request_payload


    monkeypatch.setattr(SongDB, "create", mock_post)

    response = test_app.post("/songs", data=json.dumps(test_request_payload),)

    assert response.status_code == 201
    assert response.json() == test_request_payload

def test_get_song(test_app, monkeypatch):
    test_response_payload = {"id": 3,'name': 'amim', 'artist': 'eu', 'year': 19}

    async def mock_get(session):
        return test_response_payload

    monkeypatch.setattr(SongDB, "get", mock_get)

    response = test_app.get("/songs")

    assert response.status_code == 200
    assert response.json() == test_response_payload

def test_read_song_incorrect_id(test_app, monkeypatch):
    async def mock_get(id):
        return None

    monkeypatch.setattr(SongDB, "get", mock_get)

    response = test_app.get("/songs/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Not Found"

def test_create_songs_invalid_json(test_app):
    response = test_app.post("/songs", data=json.dumps({"title": "something"}))
    assert response.status_code == 422
