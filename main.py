from typing import Any
from fastapi import FastAPI
from pydantic import BaseModel
import httpx
from httpx import Response
from settings import LAT, LON

app = FastAPI(debug=True)


class OpenMeteoResponse(BaseModel):
    latitude: float


def get_data(responce: Response) -> OpenMeteoResponse:
    return OpenMeteoResponse(**responce.json())


@app.get("/weather/")
def main_route() -> dict[str, Any]:
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": LAT,
        "longitude": LON,
        "hourly": "temperature_2m",
        "daily": "sunrise,sunset",
        "timezone": "Europe/Moscow",
    }
    try:
        response = httpx.get(url, params=params)
        data = get_data(response)
        return {"latitude": data.latitude}
    except httpx.ConnectTimeout:
        return {"error": "time out"}
