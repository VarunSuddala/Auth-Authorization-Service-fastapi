from pydantic import BaseModel, EmailStr,field_validator
import re

class UserRegister(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    
    @field_validator("password")
    def validate_password(cls, value):
        if len(value)<8:
            raise ValueError("Password must be at least 8 characters")
        if not re.search(r"[A-Z]",value):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[a-z]",value):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r"[0-9]",value):
            raise ValueError("Password must contain at least one number")
        if not re.search(r"[!@#$%^&*]",value):
            raise ValueError("Password must contain at least one special character")
        return value

class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    role: str

    class Config:
        from_attributes= True

class UserLogin(BaseModel):
    email:EmailStr
    password:str

class TokenResponse(BaseModel):
    access_token: str
    refresh_token:str
    token_type: str

