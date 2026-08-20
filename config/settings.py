import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.weather-ai.co"
WEATHER_ENDPOINT = "/v1/weather"

API_KEY = os.getenv("API_KEY")

DEFAULT_TIMEOUT = 10