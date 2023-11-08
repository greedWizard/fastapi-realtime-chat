import pytest
from dependency_injector.providers import Configuration
from faker import Faker

from domain.messages.exceptions import TextLengthTooLongError
from domain.messages.values import MessageText


def test_message_text_too_long(faker: Faker, common_config: Configuration):
    text = faker.pystr(
        common_config.messages.text_max_length() + 1,
        common_config.messages.text_max_length() + 1,
    )
    message_text = MessageText(text)

    with pytest.raises(TextLengthTooLongError):
        message_text.validate()


def test_message_text_fit(faker: Faker, common_config: Configuration):
    text = faker.pystr(
        common_config.messages.text_max_length() - 100,
        common_config.messages.text_max_length() - 1,
    )
    message_text = MessageText(text)
    message_text.validate()
