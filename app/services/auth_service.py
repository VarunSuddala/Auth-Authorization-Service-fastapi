from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.user import User
from app.schemas.user_schema import UserRegister,UserLogin
from app.core.security import hash_password
from app.core.security import verify_password,Create_token,Create_refresh_token
from fastapi.security import OAuth2PasswordRequestForm
###################################################################################
def register_user(db: Session, user_data: UserRegister) -> User:
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        return None  # User with this email already exists
    
    new_user = User(
        full_name=user_data.full_name,
        email=user_data.email,
        hashed_password=hash_password(user_data.password)
    )
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except IntegrityError:
        db.rollback()
        return None
######################################################################################## 
def login_user(data,db:Session):
    existing_user=db.query(User).filter(User.email==data.username).first()
    if not existing_user:return None

    if not verify_password(data.password,existing_user.hashed_password):
        return None
    
    token=Create_token(
        {
            "sub":str(existing_user.id),
            "email":existing_user.email,
            "role":existing_user.role
        }
    )

    refresh_token=Create_refresh_token(
        {
            "sub":str(existing_user.id)
        }
        )
    return {
        "access_token": token,
        "refresh_token":refresh_token,
        "token_type": "bearer"
    }
