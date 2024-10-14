import httpx
from httpx import Response
from main.models import OpenMeteoCity


def get_city_coordinates_response(city_name: str) -> Response | None:
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
        "name": city_name,
        "count": "1",
        "language": "ru",
        "format": "json",
    }
    try:
        return httpx.get(url, params=params)
    except httpx.ConnectTimeout:
        return None


def get_weather_response(city: OpenMeteoCity) -> Response | None:
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": str(city.latitude),
        "longitude": str(city.longitude),
        "hourly": "temperature_2m",
        "forecast_days": "1",
        "timezone": city.timezone,
    }
    try:
        return httpx.get(url, params=params)
    except httpx.ConnectTimeout:
        return None
