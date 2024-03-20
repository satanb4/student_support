from fastapi import APIRouter

from app.views.home import router as home_router


main_router = APIRouter()

main_router.include_router(home_router)

