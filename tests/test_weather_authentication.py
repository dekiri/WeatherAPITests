from utils.api_client import APIClient
from config.settings import WEATHER_ENDPOINT


def weather_params():
    return {
        "lat": -1.2921,
        "lon": 36.8219,
        "days": 3,
        "units": "metric",
        "ai": False
    }


def test_valid_api_key(api_key):
    client = APIClient(api_key=api_key)

    response = client.get(
        WEATHER_ENDPOINT,
        params=weather_params()
    )

    print("REQUEST URL:", response.url)
    print("STATUS:", response.status_code)
    print("BODY:", response.text)

    assert response.status_code == 200


def test_missing_api_key():
    client = APIClient(api_key=None)

    response = client.get(
        WEATHER_ENDPOINT,
        params=weather_params()
    )

    print("REQUEST URL:", response.url)
    print("STATUS:", response.status_code)
    print("BODY:", response.text)

    assert response.status_code == 401


def test_invalid_api_key():
    client = APIClient(api_key="invalid-api-key")

    response = client.get(
        WEATHER_ENDPOINT,
        params=weather_params()
    )

    print("REQUEST URL:", response.url)
    print("STATUS:", response.status_code)
    print("BODY:", response.text)

    assert response.status_code == 401