import json
import httpx
from fastapi import FastAPI
from pydantic import BaseModel
from httpx import Response
from settings import LAT, LON

app = FastAPI(debug=True)


class OpenMeteoData(BaseModel):
    latitude: float = 0.0


def open_meteo_data(responce: Response) -> OpenMeteoData:
    try:
        return OpenMeteoData(**responce.json())
    except json.decoder.JSONDecodeError:
        return OpenMeteoData()


def response_from_open_meteo() -> Response | None:
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": LAT,
        "longitude": LON,
        "hourly": "temperature_2m",
        "daily": "sunrise,sunset",
        "timezone": "Europe/Moscow",
    }
    try:
        return httpx.get(url, params=params)
    except httpx.ConnectTimeout:
        return None


# @app.get("/weather/")
def main_route() -> OpenMeteoData:
    response = response_from_open_meteo()
    return open_meteo_data(response)


print(main_route())
