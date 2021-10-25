from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.models.user import User, UserCreate

class RepositoryUser:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, user: UserCreate):
        user_create = User(name=user.name, email=user.email, password=user.password)
        self.session.add(user_create)
        await self.session.commit()
        await self.session.refresh(user_create)
        return user_create

    async def list_users(self):
        resp = await self.session.execute(select(User))
        users = resp.scalars().all()
        return users

    async def get_user(self, email: str):
        resp = await self.session.execute(select(User).where(User.email == email))
        user = resp.scalars().first()
        return user


        
