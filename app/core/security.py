from passlib.context import CryptContext
from jose.jwt import encode as jwtEncode,decode as jwtDecode
from jose import JWTError
pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto")
from app.core.config import settings
from datetime import datetime ,timedelta
def hash_password(password: str) -> str:
    return pwd_context.hash(password[:72])

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def Create_token(data:dict):
    encode_data=data.copy()
    expire= datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    encode_data.update({"exp":expire, "type": "access"})

    encode_jwt=jwtEncode(encode_data,
                         settings.SECRET_KEY,
                         algorithm=settings.ALGORITHM)
    return encode_jwt

def Create_refresh_token(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
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
        playload=jwtDecode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        return playload
    except JWTError:
        return None

