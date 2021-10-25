from starlette.testclient import TestClient
import json
import pytest

from app.api.crud import songs
from app.api.models.models import Song, SongCreate


def test_ping(test_app, monkeypatch):
    test_request_payload = {'name': 'amim', 'artist': 'eu', 'year': 19}
    test_response_payload = {"id": 3,'name': 'amim', 'artist': 'eu', 'year': 19}

    async def mock_post(db, song):
        return test_request_payload


    monkeypatch.setattr(songs, "song_post", mock_post)

    response = test_app.post("/songs", data=json.dumps(test_request_payload),)

    assert response.status_code == 200
    assert response.json() == test_request_payload
