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
