from fastapi import Depends, FastAPI
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.models import Song, SongCreate

app = FastAPI()


@app.get("/ping")
async def pong():
    return {"ping": "ipong!"}


@app.get("/songs", response_model=list[Song])
async def get_songs(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Song))
    songs = result.scalars().all()
    return [Song(name=song.name, artist=song.artist, year=song.year, id=song.id) for song in songs]


@app.post("/songs")
async def add_song(song: SongCreate, session: AsyncSession = Depends(get_session)):
    song_db = Song(name=song.name, artist=song.artist, year=song.year)
    session.add(song_db)
    await session.commit()
    await session.refresh(song_db)
    return song_db
