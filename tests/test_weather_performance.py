from config.settings import WEATHER_ENDPOINT


def test_weather_response_time(api_client):
    params = {
        "lat": -1.2921,
        "lon": 36.8219,
        "days": 3,
        "units": "metric",
        "ai": False
    }

    response = api_client.get(
        WEATHER_ENDPOINT,
        params=params
    )

    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 3