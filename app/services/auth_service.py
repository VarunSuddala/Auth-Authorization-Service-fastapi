from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.user import User
from app.schemas.user_schema import UserRegister
from app.core.security import hash_password

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
