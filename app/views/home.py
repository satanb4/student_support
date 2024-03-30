# title: home.py
# Author: Sayan Bandyopadhyay
# Date: 2024-03-24 20:03:22
# Description: This file contains the views that are required for Home Page of the FastAPI application.

from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse, RedirectResponse

from app.core.config import templates

# -- Fetching Test Data -- #
from app.backend.db.operations import users
from app.backend.stats import graphs

# -- END -- #

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def home_view(request: Request):
    user = None
    return templates.TemplateResponse(
        "pages/index.html",
        {"request": request, "user": user},
    )


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
    plot = graphs.gdp_data()
    return templates.TemplateResponse(
        str(plot),
        {"request": request},
    )
