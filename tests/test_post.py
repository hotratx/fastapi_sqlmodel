import json
import pdb

import pytest

from app.api.crud.songs import SongDB


#def test_create_note(test_app, monkeypatch):
#    test_request_payload = {'name': 'amim', 'artist': 'eu', 'year': 19}
#    test_response_payload = {"id": 3,'name': 'amim', 'artist': 'eu', 'year': 19}
#
#    async def mock_post(payload):
#        return test_request_payload
#
#    monkeypatch.setattr(SongDB, "create", mock_post)
#
#    response = test_app.post("/songs/", data=json.dumps(test_request_payload))
#    #pdb.set_trace()
#
#    assert response.status_code == 201
#    #assert response == test_response_payload


#def test_create_note_invalid_json(test_app):
#    response = test_app.post("/songs/", data=json.dumps({"title": "something"}))
#    assert response.status_code == 422
