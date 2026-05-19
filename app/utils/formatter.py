def get_weather_icon(condition):

    condition = condition.lower()

    if "clear" in condition:
        return "☀️"

    elif "cloud" in condition:
        return "☁️"

    elif "rain" in condition:
        return "🌧️"

    elif "snow" in condition:
        return "❄️"

    elif "storm" in condition:
        return "⛈️"

    elif "mist" in condition or "fog" in condition:
        return "🌫️"

    return "🌍"


def print_current_weather(city, data):

    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    print(f"\nCurrent Weather in {city}")
    print("-" * 40)
    print(f"Temperature : {temperature}°C")
    icon = get_weather_icon(weather)
    print(f"Condition   : {icon} {weather}")
    print(f"Humidity    : {humidity}%")
    print(f"Wind Speed  : {wind_speed} m/s")


def print_forecast(city, data):

    print(f"\n5-Day Forecast for {city}")
    print("-" * 40)

    forecasts = data["list"]

    for item in forecasts[::8]:

        date = item["dt_txt"]
        temperature = item["main"]["temp"]
        condition = item["weather"][0]["description"]

        print(date)
        print(f"Temperature : {temperature}°C")
        icon = get_weather_icon(condition)
        print(f"Condition   : {icon} {condition}")
        print("-" * 40)