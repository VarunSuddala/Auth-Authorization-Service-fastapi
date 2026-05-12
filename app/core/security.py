from passlib.context import CryptContext
from jose.jwt import encode as jwtEncode,decode as jwtDecode
from jose import JWTError
pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto")
from app.core.config import settings
from datetime import datetime, timedelta, timezone
def hash_password(password: str) -> str:
    return pwd_context.hash(password[:72])

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_token(data:dict):
    encode_data=data.copy()
    expire= datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    encode_data.update({"exp":expire, "type": "access"})

    encode_jwt=jwtEncode(encode_data,
                         settings.SECRET_KEY,
                         algorithm=settings.ALGORITHM)
    return encode_jwt

def create_refresh_token(data:dict):
    to_encode=data.copy()
    expire=datetime.now(timezone.utc)+timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update(
        {
            "exp":expire,
            "type":"refresh"
        }
    )

    refresh_token=jwtEncode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM

    )

    return refresh_token


def verify_access_token(token:str):
    try:
        payload=jwtDecode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        if payload.get("type")!="access":return None
        return payload
    except JWTError:
        return None



def verify_refresh_token(token:str):
    try:
        payload=jwtDecode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        if payload.get("type")!="refresh":return None
        return payload
    except JWTError:
        return None
