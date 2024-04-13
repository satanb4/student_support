# title: search.py
# Author: Finn Lestrange
# Date: 2024-04-13 14:11:45
# Description: This file contains the views that are required for Search Functionality.

from fastapi import APIRouter
from fastapi import Form
from fastapi.responses import HTMLResponse


router = APIRouter()


@router.post("/search_results", response_class=HTMLResponse)
async def search_view(query: str = Form()):
    # TODO: search logic to be implemented here
    return "<div>Search Results for " + query + "</div>"
