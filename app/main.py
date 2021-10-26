from fastapi import FastAPI

from app.api.routers import ping, song, auth

app = FastAPI()

app.include_router(ping.router)
app.include_router(song.router)
app.include_router(auth.router, prefix="/auth")

    #result = await session.execute(select(Song))
    #songs = result.scalars().all()
    #return [Song(name=song.name, artist=song.artist, year=song.year, id=song.id) for song in songs]

@app.post("/vai")
async def add_test():
    return {'foi': 18}
