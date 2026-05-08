from pydantic import BaseModel, EmailStr,field_validator


class UserRegister(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    
    @field_validator("password")
    def validate_password(cls, value):
        if len(value)<6:
            raise ValueError("Password must be at least 6 characters")
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
