import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_1_URL: str = os.getenv('API_1_URL', "")
    API_2_URL: str = os.getenv('API_2_URL', "")
    API_3_URL: str = os.getenv('API_3_URL', "")

settings = Settings()