from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.api.models.models import Song, SongCreate, SongBase
from app.api.crud import songs

router = APIRouter()

@router.get("/songs")
async def get_songs(session: AsyncSession = Depends(get_session)):
    response = await songs.song_get(session)
    return response

@router.post("/songs", response_model=SongBase)
async def add_song(song: SongCreate, session: AsyncSession = Depends(get_session)):
    response = await songs.song_post(session, song)
    #response = await SongDB(session).create(song)
    return response
