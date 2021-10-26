from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.api.models.user import UserBase, UserCreate, LoginData, LoginSuccess
from app.api.crud.auth import RepositoryUser
from app.infra.providers.hash_provider import gerar_hash, verificar_hash
from app.infra.providers import token_provider 
from app.api.routers.auth_utils import obter_usuario_logado

router = APIRouter()

@router.post("/signup", 
        response_model=UserBase,
        status_code=status.HTTP_201_CREATED)
async def signup(user: UserCreate, session: AsyncSession = Depends(get_session)):
    user_exist = await RepositoryUser(session).user_by_email(user.email)
    if user_exist:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"O email {user.email} já foi cadastrado.")

    hash_password = gerar_hash(user.password)
    user.password = hash_password
    user_create = await RepositoryUser(session).create(user)
    return user_create
    
@router.get("/users", response_model=List[UserBase])
async def users_list(session: AsyncSession = Depends(get_session)):
    users = await RepositoryUser(session).list_users()
    return users

@router.get("/user/{email}")
async def get_user(email: str, session: AsyncSession = Depends(get_session)):
    user = await RepositoryUser(session).user_by_email(email)
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                detail="Usuário não cadastrado")
    return user

@router.post("/login", response_model=LoginSuccess)
async def login_user(user: LoginData, session: AsyncSession = Depends(get_session)):
    user_exist = await RepositoryUser(session).user_by_email(user.email) 
    if not user_exist:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Usuário não existe.")

    password_valid = verificar_hash(user.password, user_exist.password)
    if not password_valid:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Senha incorreta.")
    
    # Gerar token
    token = token_provider.create_access_token({"sub": user_exist.email})
    return LoginSuccess(user_base=user_exist, access_token=token)

@router.get("/me", response_model=UserBase)
def me(user: UserBase = Depends(obter_usuario_logado)):
    return user
