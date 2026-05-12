from fastapi import APIRouter, Depends, HTTPException,status,Query
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas.user_schema import UserRegister,UserResponse,UserLogin,TokenResponse
from app.services.auth_service import register_user,login_user,create_new_access_token,logout_user
from app.api.deps import get_current_user
from app.models.user import User
from app.core.security import verify_access_token,verify_refresh_token
from fastapi.security import OAuth2PasswordRequestForm

router =APIRouter(prefix="/auth", tags=["authentication"])


@router.post("/register",response_model=UserResponse)
def create_user(user:UserRegister,db:Session=Depends(get_db)):
    new_user=register_user(db,user)

    if not new_user:raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Email already registered ")
    
    return new_user

@router.post("/login",response_model=TokenResponse)
def login(user:OAuth2PasswordRequestForm = Depends(),db:Session=Depends(get_db)):

    token=login_user(user,db)
     
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid email or password")
    return token


@router.get("/me")
def get_me(user:User = Depends(get_current_user)):

    return {
        "id": user.id,
        "full_name": user.full_name,
        "email": user.email,
        "role": user.role
    }

@router.post("/refresh")
def refresh_token (token:str=Query(...),db:Session = Depends(get_db) ):

    payload=verify_refresh_token(token)
    if not payload: raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid refresh token")

    user=db.query(User).filter(User.id==payload.get("sub")).first()
    if not user: raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid refresh token")
    if user.refresh_token != token: raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid refresh token")
    new_access_token = create_new_access_token(user, db)
    
    return {
        "access_token": new_access_token,
        "refresh_token": token,
        "token_type": "bearer"
    }

    
@router.post("/logout")
def logout(current_user=Depends(get_current_user),db:Session=Depends(get_db)):
    success=logout_user(db,current_user.id)

    if not success:raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid refresh token")

    return {"message":"Logout success"}