from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASES_ENGINE:str
    DATABASES_NAME:str
    DATABASES_USER:str
    DATABASES_PASSWORD:str
    DATABASES_HOST:str
    DATABASES_PORT:str
    
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore'
    )
    
@lru_cache
def get_settings():
    return Settings()