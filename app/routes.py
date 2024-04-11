from fastapi import APIRouter

from app.views.home import router as home_router
from app.views.user import router as user_router


main_router = APIRouter()

main_router.include_router(home_router)
main_router.include_router(user_router)

