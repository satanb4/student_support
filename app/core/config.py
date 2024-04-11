# title: config.py
# Author: Sayan Bandyopadhyay
# Date: 2024-03-24 20:02:50
# Description: This file contains the configuration settings for the FastAPI application.

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

ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS", cast=CommaSeparatedStrings, default=""
)

DATABASE_URL = config(
    "DATABASE_URL",
    default="postgresql+asyncpg://postgres:postgres@db:5432/mypath_test",
)

template_base_dir = f"app/templates"
templates = Jinja2Templates(directory=template_base_dir)

# Database
# DATABASE_URL = config("DATABASE_URL", default="postgresql+asyncpg://postgres:postgres@db:5432/mydatabase")
