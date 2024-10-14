from typing import Any
from dataclasses import dataclass
from datetime import datetime
from httpx import Response
from main.models import OpenMeteoData, OpenMeteoCity


@dataclass
class MainData:
    latitude: float
    longitude: float
    timezone: str
    temperature: float


def fetch_open_meteo_city(responce: Response | None) -> OpenMeteoCity:
    if responce:
        data = responce.json()
        if data:
            results = data.get("results")
            if results and len(results) > 0:
                return OpenMeteoCity(**results[0])
    return OpenMeteoCity()


def fetch_main_data(data: dict[str, Any]) -> MainData:
    latitude = data.get("latitude", 0.0)
    longitude = data.get("longitude", 0.0)
    timezone = data.get("timezone", "")
    temperature = 0.0
    hourly = data.get("hourly")
    if hourly:
        temperature_2m = hourly.get("temperature_2m")
        if temperature_2m:
            temperature = temperature_2m[datetime.now().hour]
    return MainData(latitude, longitude, timezone, temperature)


def fetch_open_meteo_data(responce: Response | None) -> OpenMeteoData:
    if responce:
        data = responce.json()
        if data:
            main_data = fetch_main_data(data)
            return OpenMeteoData(
                latitude=main_data.latitude,
                longitude=main_data.longitude,
                timezone=main_data.timezone,
                temperature=main_data.temperature,
            )
    return OpenMeteoData()
