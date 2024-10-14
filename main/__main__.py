import uvicorn
from fastapi import FastAPI
from main.models import OpenMeteoData
from main.responses import (
    get_weather_response,
    get_city_coordinates_response,
)
from main.fethers import fetch_open_meteo_data, fetch_open_meteo_city

app = FastAPI(debug=True)


@app.get("/weather/{city_name}")
def main_route(city_name: str) -> OpenMeteoData:
    city = fetch_open_meteo_city(get_city_coordinates_response(city_name))
    return fetch_open_meteo_data(get_weather_response(city))


if __name__ == "__main__":
    uvicorn.run(app)
