from typing import Optional

from sqlmodel import SQLModel, Field


class UserBase(SQLModel):
    name: Optional[str]
    email: str


class User(UserBase, table=True):
    id: int = Field(default=None, primary_key=True)
    password: str


class UserCreate(UserBase):
    password: str


class LoginUser(SQLModel):
    email: str
    password: str
