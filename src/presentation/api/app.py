from dependency_injector.wiring import Provide, inject
from fastapi import FastAPI

from domain.common.containers import CommonContainer
from infrastructure.dependencies.initialization import init_dependencies


@inject
def create_app(
    debug: bool = Provide[CommonContainer.config.debug],
):
    init_dependencies()

    return FastAPI(
        debug=debug,
        title='FastAPI Messages Services',
        docs_url='/api/docs',
    )
