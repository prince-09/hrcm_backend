from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGODB_URI: str
    MONGODB_DB: str

    class Config:
        env_file = ".env"

settings = Settings()
