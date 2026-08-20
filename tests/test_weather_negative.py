import pytest

from config.settings import WEATHER_ENDPOINT


@pytest.mark.parametrize(
    "params",
    [
        {
            "lon": 36.8219,
            "days": 3,
            "units": "metric",
            "ai": False
        },
        {
            "lat": -1.2921,
            "days": 3,
            "units": "metric",
            "ai": False
        },
        {
            "days": 3,
            "units": "metric",
            "ai": False
        },
    ],
    ids=[
        "missing_lat",
        "missing_lon",
        "missing_lat_and_lon"
    ]
)
def test_missing_coordinates(api_client, params):
    response = api_client.get(
        WEATHER_ENDPOINT,
        params=params
    )

    assert response.status_code >= 400

    body = response.json()

    assert isinstance(body, dict)
    assert body


@pytest.mark.parametrize(
    "lat",
    [-91, 91]
)
def test_invalid_latitude(api_client, lat):
    params = {
        "lat": lat,
        "lon": 36.8219,
        "days": 3,
        "units": "metric",
        "ai": False
    }

    response = api_client.get(
        WEATHER_ENDPOINT,
        params=params
    )

    assert response.status_code >= 400

    body = response.json()

    assert isinstance(body, dict)
    assert body


@pytest.mark.parametrize(
    "lon",
    [-181, 181]
)
def test_invalid_longitude(api_client, lon):
    params = {
        "lat": -1.2921,
        "lon": lon,
        "days": 3,
        "units": "metric",
        "ai": False
    }

    response = api_client.get(
        WEATHER_ENDPOINT,
        params=params
    )

    assert response.status_code >= 400

    body = response.json()

    assert isinstance(body, dict)
    assert body


@pytest.mark.parametrize(
    "days",
    [0, -1, 4, 10, "invalid"]
)
def test_invalid_days(api_client, days):
    params = {
        "lat": -1.2921,
        "lon": 36.8219,
        "days": days,
        "units": "metric",
        "ai": False
    }

    response = api_client.get(
        WEATHER_ENDPOINT,
        params=params
    )

    assert response.status_code <= 400

    body = response.json()

    assert isinstance(body, dict)
    assert body


def test_invalid_units(api_client):
    params = {
        "lat": -1.2921,
        "lon": 36.8219,
        "days": 3,
        "units": "invalid",
        "ai": False
    }

    response = api_client.get(
        WEATHER_ENDPOINT,
        params=params
    )

    assert response.status_code <= 400

    body = response.json()

    assert isinstance(body, dict)
    assert body


@pytest.mark.parametrize(
    "ai",
    ["true", "false", "invalid", 123]
)
def test_invalid_ai(api_client, ai):
    params = {
        "lat": -1.2921,
        "lon": 36.8219,
        "days": 3,
        "units": "metric",
        "ai": ai
    }

    response = api_client.get(
        WEATHER_ENDPOINT,
        params=params
    )

    assert response.status_code <= 400

    body = response.json()

    assert isinstance(body, dict)
    assert body