# title: search.py
# Author: Finn Lestrange
# Date: 2024-04-13 14:11:45
# Description: This file contains the views that are required for Search Functionality.

from fastapi import APIRouter
from fastapi import Form, Request
from fastapi.responses import HTMLResponse
from app.core.config import templates


router = APIRouter()


@router.post("/search_results", response_class=HTMLResponse)
async def search_view(request: Request):
    # TODO: search logic to be implemented here
    return templates.TemplateResponse(
        "partials/search/sample-results.html",
        {"request": request},
    )
