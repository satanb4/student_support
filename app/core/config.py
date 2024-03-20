from typing import List
from pathlib import Path

from fastapi.templating import Jinja2Templates
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

main_dir = Path(__file__).resolve().parent.parent.parent
config = Config(f"{main_dir}/.env")

PROJECT_NAME = config(
    "MYPATH",
    default="MyPath v0.1 🔥",
)
SECRET_KEY = config("SECRET_KEY", default="secret")

DEBUG = config("DEBUG", cast=bool, default=False)

ALLOWED_HOSTS: List[str] = config("ALLOWED_HOSTS", cast=CommaSeparatedStrings, default="")

templates = Jinja2Templates(directory="app/templates")

# Database
# DATABASE_URL = config("DATABASE_URL", default="postgresql+asyncpg://postgres:postgres@db:5432/mydatabase")