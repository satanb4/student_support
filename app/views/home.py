from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse, RedirectResponse

from pydantic import BaseModel, Field

from app.core.config import templates

router = APIRouter()


class userModel(BaseModel):
    # Sample model to use until we have a database
    id: int
    username: str
    email: str
    user_type: str


users = [
    userModel(
        id=1, username="John Doe", email="johndoe@example.com", user_type="staff"
    ),
    userModel(
        id=2, username="Jane Doe", email="janedoe@example.com", user_type="student"
    ),
    userModel(
        id=3, username="John Smith", email="johnsmith@example.com", user_type="staff"
    ),
]


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


@router.post("/clicked", response_class=HTMLResponse)
async def clicked_view(request: Request):
    return templates.TemplateResponse(
        "partials/clicked.html",
        {"request": request},
    )
