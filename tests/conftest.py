import pytest

from config.settings import API_KEY
from utils.api_client import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def api_key():
    return API_KEY