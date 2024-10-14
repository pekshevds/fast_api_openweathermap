from pydantic import BaseModel


class OpenMeteoCity(BaseModel):
    latitude: float = 0.0
    longitude: float = 0.0
    timezone: str = ""
    name: str = ""


class OpenMeteoData(BaseModel):
    latitude: float = 0.0
    longitude: float = 0.0
    timezone: str = ""
    temperature: float = 0.0
