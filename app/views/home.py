from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse

from app.core.config import templates

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def home_view(request: Request):
    return templates.TemplateResponse(
        "pages/index.html",
        {"request": request},
    )

@router.post("/clicked", response_class=HTMLResponse)
async def clicked_view(request: Request):
    return templates.TemplateResponse(
        "partials/clicked.html",
        {"request": request},
    )