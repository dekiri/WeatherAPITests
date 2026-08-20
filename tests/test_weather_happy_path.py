import pytest

from config.settings import WEATHER_ENDPOINT


@pytest.mark.parametrize(
    "units",
    ["metric", "imperial"]
)
def test_get_weather_units(api_client, units):
    params = {
        "lat": -1.2921,
        "lon": 36.8219,
        "days": 3,
        "units": units,
        "ai": False
    }

    response = api_client.get(
        WEATHER_ENDPOINT,
        params=params
    )

    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith("application/json")

    body = response.json()

    assert isinstance(body, dict)
    assert body

    assert body["lat"] == -1.2921
    assert body["lon"] == 36.8219
    assert body["units"] == units
    assert body["days"] == 3

    assert "current" in body
    assert "daily" in body
    assert "hourly" in body


@pytest.mark.parametrize(
    "ai_enabled",
    [True, False]
)
def test_get_weather_ai(api_client, ai_enabled):
    params = {
        "lat": -1.2921,
        "lon": 36.8219,
        "days": 3,
        "units": "metric",
        "ai": ai_enabled
    }

    response = api_client.get(
        WEATHER_ENDPOINT,
        params=params
    )

    print("\nAI:", ai_enabled)
    print("Status:", response.status_code)
    print("Response:", response.json())

    assert response.status_code == 200

    body = response.json()

    assert isinstance(body, dict)
    assert "ai_summary" in body


@pytest.mark.parametrize(
    "days",
    [1, 3]
)
def test_get_weather_forecast_days(api_client, days):
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

    assert response.status_code == 200

    body = response.json()

    assert body["days"] == days
    assert isinstance(body["daily"], list)
    assert len(body["daily"]) == days