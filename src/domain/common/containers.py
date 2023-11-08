from dependency_injector import providers
from dependency_injector.containers import (
    DeclarativeContainer,
    WiringConfiguration,
)


class CommonContainer(DeclarativeContainer):
    wiring_config: WiringConfiguration = WiringConfiguration(
        packages=('domain',),
        auto_wire=False,
    )

    config = providers.Configuration(strict=True)
