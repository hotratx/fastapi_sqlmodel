from fastapi import Depends, FastAPI, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.api.models.models import Song, SongCreate
from app.api import ping
from app.api.crud.post import Post

app = FastAPI()

app.include_router(ping.router)

@app.get("/songs", response_model=list[Song])
async def get_songs(session: AsyncSession = Depends(get_session)):
    response = await Post(session).get()
    return response
    #result = await session.execute(select(Song))
    #songs = result.scalars().all()
    #return [Song(name=song.name, artist=song.artist, year=song.year, id=song.id) for song in songs]


@app.post("/songs", status_code=status.HTTP_201_CREATED)
async def add_song(song: SongCreate, session: AsyncSession = Depends(get_session)):
    response = await Post(session).create(song)
    return response
