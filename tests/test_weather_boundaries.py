import pytest

from config.settings import WEATHER_ENDPOINT


@pytest.mark.parametrize(
    "lat",
    [-90, 90]
)
def test_latitude_valid_boundaries(api_client, lat):
    params = {
        "lat": lat,
        "lon": 36.8219,
        "days": 1,
        "units": "metric",
        "ai": False
    }

    response = api_client.get(
        WEATHER_ENDPOINT,
        params=params
    )

    assert response.status_code == 200

    body = response.json()

    assert body["lat"] == lat


@pytest.mark.parametrize(
    "lat",
    [-91, 91]
)
def test_latitude_invalid_boundaries(api_client, lat):
    params = {
        "lat": lat,
        "lon": 36.8219,
        "days": 1,
        "units": "metric",
        "ai": False
    }

    response = api_client.get(
        WEATHER_ENDPOINT,
        params=params
    )

    assert response.status_code >= 400


@pytest.mark.parametrize(
    "lon",
    [-180, 180]
)
def test_longitude_valid_boundaries(api_client, lon):
    params = {
        "lat": -1.2921,
        "lon": lon,
        "days": 1,
        "units": "metric",
        "ai": False
    }

    response = api_client.get(
        WEATHER_ENDPOINT,
        params=params
    )

    assert response.status_code == 200

    body = response.json()

    assert body["lon"] == lon


@pytest.mark.parametrize(
    "lon",
    [-181, 181]
)
def test_longitude_invalid_boundaries(api_client, lon):
    params = {
        "lat": -1.2921,
        "lon": lon,
        "days": 1,
        "units": "metric",
        "ai": False
    }

    response = api_client.get(
        WEATHER_ENDPOINT,
        params=params
    )

    assert response.status_code >= 400