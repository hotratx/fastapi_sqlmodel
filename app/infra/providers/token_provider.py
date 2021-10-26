from jose import jwt
from datetime import datetime, timedelta

#CONFIG
SECRET_KEY = "a21e51b95e38e5bf58a3347f824f9e4a"
ALGORITHM = "HS256"
EXPIRES_IN_MIN = 30


def create_access_token(data: dict):
    """:data = { "sub": email }
    Retorna o dict com o dict data contendo a chave exp com a data de expiração"""
    data = data.copy()
    expiration = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)
    data.update({"exp": expiration})

    token_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return token_jwt
    

def verify_access_token(token: str):
    """Retorna apenas o sub que contém o email, para
    poder identificar o usuário."""
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload.get("sub")
