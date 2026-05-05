from app.db.database import session_local
from sqlalchemy.orm import session
from app.models.user import User
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException,status
from app.core.security import verify_access_token

Oauth2_schema=OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_db():
    db=session_local()

    try:
        yield db
    finally:
        db.close()

def get_current_user(token:str = Depends(Oauth2_schema),db:session=Depends(get_db)):

    payload=verify_access_token(token)
    if payload is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
    
    user_id=int(payload.get("sub"))

    user=db.query(User).filter(user_id==User.id).first()

    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="User not found")
    
    return user