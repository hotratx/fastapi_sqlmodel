from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.api.models.models import Song, SongCreate, SongBase
from app.api.crud import songs
from app.api.crud.songs import SongDB

router = APIRouter()

@router.get("/songs")
async def get_songs(session: AsyncSession = Depends(get_session)):
    response = await SongDB(session).get()
    return response

@router.post("/songs", response_model=SongBase, status_code=status.HTTP_201_CREATED)
async def add_song(song: SongCreate, session: AsyncSession = Depends(get_session)):
    response = await SongDB(session).create(song)
    return response
