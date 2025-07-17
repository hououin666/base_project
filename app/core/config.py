from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings


class RunConfig(BaseModel):
    host: str = '0.0.0.0'
    port: int = 8000


class DatabaseConfig(BaseModel):
    url: PostgresDsn =  'postgresql+asyncpg'
    echo: bool = False
    echo_pool: bool = False
    max_overflow: int = 10
    pool_size: int = 50


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    db: DatabaseConfig

settings = Settings()
