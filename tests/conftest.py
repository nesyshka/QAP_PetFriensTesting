import pytest

from api import PetFriendsTest
from settings import valid_email, valid_password


@pytest.fixture(scope="session")
def api_key() -> str:
    _, api_key = PetFriendsTest().get_api_key(valid_email, valid_password)
    yield api_key

