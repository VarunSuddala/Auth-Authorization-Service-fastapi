from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_DAYS:int
    # Brute-force / lockout policy
    MAX_LOGIN_ATTEMPTS: int = 5       # failed attempts before lockout
    LOCKOUT_MINUTES: int = 15         # how long the account stays locked

    class Config:
        env_file = ".env"

settings = Settings()


