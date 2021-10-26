from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer

from app.api.crud.auth import RepositoryUser
from app.db import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from app.infra.providers import token_provider 
from jose import JWTError


oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")


async def obter_usuario_logado(token: str = Depends(oauth2_schema),
        session: AsyncSession = Depends(get_session)):
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="Toke inválido")
    try: 
        email = token_provider.verify_access_token(token)
    except JWTError: 
        raise exception

    if not email:
        raise exception

    user = await RepositoryUser(session).user_by_email(email)

    if not user:
        raise exception

    return user
