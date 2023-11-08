import os

from domain.containers import common_container


def init_dependencies():
    common_container.config.from_yaml(os.environ['CONFIG_FILE'])
    common_container.wire()
