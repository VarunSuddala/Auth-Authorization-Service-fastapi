from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas.user_schema import UserRegister,UserResponse
from app.services.auth_service import register_user


router =APIRouter(prefix="/auth", tags=["authentication"])


@router.post("/register",response_model=UserResponse)
def CreateUser(user:UserRegister,db:Session=Depends(get_db)):
    new_user=register_user(db,user)

    if not new_user:raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Email already registered ")
    
    return new_user