from typing import Union

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from app.routes import main_router
from app.core import config


def get_application() -> FastAPI:
    application = FastAPI(title=config.PROJECT_NAME, debug=config.DEBUG)

    # CORS protection
    application.add_middleware(
        CORSMiddleware,
        allow_origins=config.ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(main_router)
    # print(application.routes)
    application.mount(
        "/static",
        StaticFiles(directory="app/src"),
        name="static",
    )

    return application


app = get_application()
