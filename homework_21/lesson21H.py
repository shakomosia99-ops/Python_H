import requests


def get_coordinates(city):
    """API 1: city name -> (latitude, longitude), or None if not found."""
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city, "count": 1}

    response = requests.get(url, params=params)
    data = response.json()

    if "results" not in data:
        return None

    result = data["results"][0]
    return result["latitude"], result["longitude"]


def get_weather(latitude, longitude):
    """API 2: coordinates -> current weather data (dict)."""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m",
        "timezone": "auto",
    }

    response = requests.get(url, params=params)
    return response.json()


def main():
    city = input("Enter city name: ")

    coordinates = get_coordinates(city)
    if coordinates is None:
        print("City not found")
        return

    latitude, longitude = coordinates
    weather = get_weather(latitude, longitude)
    current = weather["current"]

    print(f"City: {city}")
    print(f"Temperature: {current['temperature_2m']} °C")
    print(f"Wind Speed: {current['wind_speed_10m']} km/h")
    print(f"Time: {current['time']}")


main()
