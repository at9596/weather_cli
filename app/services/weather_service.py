import requests

from app.config import (
    API_KEY,
    CURRENT_WEATHER_URL,
    FORECAST_URL
)


def fetch_current_weather(city):

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(
        CURRENT_WEATHER_URL,
        params=params
    )

    return response.json()


def fetch_forecast(city):

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(
        FORECAST_URL,
        params=params
    )

    return response.json()