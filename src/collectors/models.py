"""
Описание моделей данных (DTO).
"""

from pydantic import Field, BaseModel
from datetime import datetime


class HashableBaseModel(BaseModel):
    """
    Добавление хэшируемости для моделей.
    """

    def __hash__(self) -> int:
        return hash((type(self),) + tuple(self.__dict__.values()))


class LocationDTO(HashableBaseModel):
    """
    Модель локации для получения сведений о погоде.

    .. code-block::

        LocationDTO(
            capital="Mariehamn",
            alpha2code="AX",
        )
    """

    capital: str
    alpha2code: str = Field(min_length=2, max_length=2)  # country alpha‑2 code


class CurrencyInfoDTO(HashableBaseModel):
    """
    Модель данных о валюте.

    .. code-block::

        CurrencyInfoDTO(
            code="EUR",
        )
    """

    code: str


class LanguagesInfoDTO(HashableBaseModel):
    """
    Модель данных о языке.

    .. code-block::

        LanguagesInfoDTO(
            name="Swedish",
            native_name="svenska"
        )
    """

    name: str
    native_name: str


class CountryDTO(BaseModel):
    """
    Модель данных о стране.

    .. code-block::

        CountryDTO(
            capital="Mariehamn",
            alpha2code="AX",
            alt_spellings=[
              "AX",
              "Aaland",
              "Aland",
              "Ahvenanmaa"
            ],
            currencies={
                CurrencyInfoDTO(
                    code="EUR",
                )
            },
            flag="http://assets.promptapi.com/flags/AX.svg",
            languages={
                LanguagesInfoDTO(
                    name="Swedish",
                    native_name="svenska"
                )
            },
            name="\u00c5land Islands",
            population=28875,
            subregion="Northern Europe",
            timezones=[
                "UTC+02:00",
            ],
            square=50453.1,
            geographical_latitude=45.23,
            geographical_longitude=15.35,
        )
    """

    capital: str
    alpha2code: str
    alt_spellings: list[str]
    currencies: set[CurrencyInfoDTO]
    flag: str
    languages: set[LanguagesInfoDTO]
    name: str
    population: int
    subregion: str
    timezones: list[str]
    square: float | None
    geographical_latitude: float | None
    geographical_longitude: float | None


class CurrencyRatesDTO(BaseModel):
    """
    Модель данных о курсах валют.

    .. code-block::

        CurrencyRatesDTO(
            base="RUB",
            date="2022-09-14",
            rates={
                "EUR": 0.016503,
            }
        )
    """

    base: str
    date: str
    rates: dict[str, float]


class WeatherInfoDTO(BaseModel):
    """
    Модель данных о погоде.

    .. code-block::

        WeatherInfoDTO(
            temp=13.92,
            pressure=1023,
            humidity=54,
            wind_speed=4.63,
            description="scattered clouds",
        )
    """

    offset_seconds: int
    timezone: int
    temp: float
    pressure: int
    humidity: int
    wind_speed: float
    description: str
    visibility: int


class NewsInfoDTO(BaseModel):
    """
    Модель данных новостей.
    .. code-block::
        NewsDTO(
            source="CNN",
            title="The latest news about the coronavirus pandemic",
            description="The latest news about the coronavirus pandemic",
            url="https://www.cnn.com/world/live-news/coronavirus-pandemic-09-14-21-intl/index.html",
            published_at="2021-09-14T20:00:00Z",
            content="The latest news about the coronavirus pandemic"
        )
    """

    source: str
    title: str
    description: str
    url: str
    published_at: datetime
    content: str


class LocationInfoDTO(BaseModel):
    """
    Модель данных для представления общей информации о месте.

    .. code-block::

        LocationInfoDTO(
            location=CountryDTO(
                capital="Mariehamn",
                alpha2code="AX",
                alt_spellings=[
                  "AX",
                  "Aaland",
                  "Aland",
                  "Ahvenanmaa"
                ],
                currencies={
                    CurrencyInfoDTO(
                        code="EUR",
                    )
                },
                flag="http://assets.promptapi.com/flags/AX.svg",
                languages={
                    LanguagesInfoDTO(
                        name="Swedish",
                        native_name="svenska"
                    )
                },
                name="\u00c5land Islands",
                population=28875,
                subregion="Northern Europe",
                timezones=[
                    "UTC+02:00",
                ],
            ),
            weather=WeatherInfoDTO(
                temp=13.92,
                pressure=1023,
                humidity=54,
                wind_speed=4.63,
                description="scattered clouds",
            ),
            currency_rates={
                "EUR": 0.016503,
            },
        )
    """

    location: CountryDTO
    weather: WeatherInfoDTO
    currency_rates: dict[str, float]
    news: list[NewsInfoDTO] | None
