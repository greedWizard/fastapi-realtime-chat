from dependency_injector.wiring import Provide, inject
from fastapi import FastAPI

from domain.common.containers import CommonContainer
from logic.dependencies.initialization import init_dependencies
from presentation.api.v1.chat.handlers import router as chat_router

API_V1_PREFIX = '/api/v1'


@inject
def create_app(
    debug: bool = Provide[CommonContainer.config.debug],
):
    init_dependencies()

    app = FastAPI(
        debug=debug,
        title='FastAPI Messages Services',
        docs_url='/api/docs',
    )
    app.include_router(chat_router, prefix=API_V1_PREFIX)
    return app
