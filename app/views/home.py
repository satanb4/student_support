# title: home.py
# Author: Sayan Bandyopadhyay
# Date: 2024-03-24 20:03:22
# Description: This file contains the views that are required for Home Page of the FastAPI application.

from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse, RedirectResponse

from app.core.config import templates

# -- Fetching Test Data -- #
from app.backend.db.mockdb import users
# -- END -- #

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def home_view(request: Request):
    user = None
    return templates.TemplateResponse(
        "pages/index.html",
        {"request": request, "user": user},
    )
