# title: user.py
# Author: Sayan Bandyopadhyay
# Date: 2024-04-09 17:31:18
# Description: This file contains the views that are required for User Page of the FastAPI application.

from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse, RedirectResponse

from app.core.config import templates
from app.backend.db.operations import users
from app.backend.stats import graphs

router = APIRouter()

# These are testing routes for different page views
@router.get("/user/{id}", response_class=HTMLResponse)
async def login(request: Request, id: int):
    for user in users:
        if user.id == id:
            return templates.TemplateResponse(
                "pages/index.html",
                {"request": request, "user": user},
            )
    else:
        return RedirectResponse("/", status_code=303)


@router.get("/graph", response_class=HTMLResponse)
async def graph_view(request: Request):
    plot = graphs.grade_data()
    return templates.TemplateResponse(
        str(plot),
        {"request": request},
    )
