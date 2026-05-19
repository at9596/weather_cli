import argparse
import requests
import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)

        data = response.json()

        if response.status_code != 200:
            print(f"Error: {data.get('message')}")
            return

        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"\nWeather in {city}")
        print("-" * 30)
        print(f"Temperature : {temperature}°C")
        print(f"Condition   : {weather}")
        print(f"Humidity    : {humidity}%")
        print(f"Wind Speed  : {wind_speed} m/s")

    except requests.exceptions.RequestException as error:
        print(f"Request failed: {error}")


parser = argparse.ArgumentParser(
    description="Weather CLI App"
)

parser.add_argument(
    "city",
    help="Enter city name"
)

args = parser.parse_args()

get_weather(args.city)