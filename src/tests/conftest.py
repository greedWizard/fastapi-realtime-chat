import pytest
from faker import Faker

from domain.containers import common_container
from logic.dependencies.initialization import init_dependencies


@pytest.fixture(scope='session')
def faker() -> Faker:
    return Faker('ru')


@pytest.fixture(scope='session', autouse=True)
def setup_tests_containers():
    init_dependencies()


@pytest.fixture(scope='session')
def common_config():
    return common_container.config
