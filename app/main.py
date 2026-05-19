import argparse

from app.services.weather_service import (
    fetch_current_weather,
    fetch_forecast
)

from app.utils.formatter import (
    print_current_weather,
    print_forecast
)


def main():

    parser = argparse.ArgumentParser(
        description="Weather CLI App"
    )

    parser.add_argument(
        "city",
        help="Enter city name"
    )

    parser.add_argument(
        "--forecast",
        action="store_true",
        help="Show 5-day forecast"
    )

    args = parser.parse_args()

    if args.forecast:

        data = fetch_forecast(args.city)

        if data.get("cod") != "200":
            print(f"Error: {data.get('message')}")
            return

        print_forecast(args.city, data)

    else:

        data = fetch_current_weather(args.city)

        if data.get("cod") != 200:
            print(f"Error: {data.get('message')}")
            return

        print_current_weather(args.city, data)