from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.models.models import Song, SongCreate


class SongDB():
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, song: SongCreate):
        song_db = Song(name=song.name, artist=song.artist, year=song.year)
        self.session.add(song_db)
        await self.session.commit()
        await self.session.refresh(song_db)
        return song_db

    async def get(self):
        resp = await self.session.execute(select(Song))
        songs = resp.scalars().all()
        #return [Song(name=song.name, artist=song.artist, year=song.year, id=song.id) for song in songs]
        return songs
