from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.api.models.models import Song, SongCreate


class Post():
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, song: SongCreate):
        song_db = Song(name=song.name, artist=song.artist, year=song.year)
        self.db.add(song_db)
        await self.db.commit()
        await self.db.refresh(song_db)
        return song_db

    async def get(self):
        resp = await self.db.execute(select(Song))
        songs = resp.scalars().all()
        #return [Song(name=song.name, artist=song.artist, year=song.year, id=song.id) for song in songs]
        return songs


