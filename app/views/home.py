from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse, RedirectResponse

from app.core.config import templates

# -- Fetching Test Data -- #
from app.backend.db.operations import users
from app.backend.stats.graphs import create_data

# -- END -- #

router = APIRouter()

plot = create_data()
print(plot)


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
    return templates.TemplateResponse(
        "partials/graphs/test_plot.html",
        {"request": request},
    )


@router.post("/clicked", response_class=HTMLResponse)
async def clicked_view(request: Request):
    return templates.TemplateResponse(
        "partials/clicked.html",
        {"request": request},
    )
