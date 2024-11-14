# pylint: disable=unused-argument
from datetime import datetime, timedelta
from typing import List, Dict
from pprint import pprint

# Mock location database
LOCATION_DB = {
    "Austin": [30.2672, -97.7431],
    "Austin Airport": [30.2021, -97.6686],
    "New York": [40.7128, -74.0060],
    "San Francisco": [37.7749, -122.4194],
    "Menlo Park": [37.4530, -122.1826],
    "Palo Alto": [37.4419, -122.1430],
    "Honolulu Hawaii": [21.3069, -157.8583],
    "Honolulu": [21.3069, -157.8583],
    "Hawaii": [19.8968, -155.5828],
    "Albany NY": [42.6526, -73.7562],
    "Berlin": [52.5200, 13.4050],
    "London": [51.5072, 0.1276],
    "Kiev": [50.4504, 30.5245],
    "Tokyo": [35.6762, 139.6503],
}

# Mock database of weather stations
STATIONS_DB = {
    (30.2672, -97.7431): [
        {"station_id": "KATT", "name": "Austin Station", "distance": 1.2},
    ],
    (30.2021, -97.6686): [
        {"station_id": "KAUS", "name": "Austin Airport Station", "distance": 0.5},
    ],
    (40.7128, -74.0060): [
        {"station_id": "KNYC", "name": "New York Central Station", "distance": 0.5},
    ],
    (37.7749, -122.4194): [
        {
            "station_id": "KSFO",
            "name": "San Francisco Airport Station",
            "distance": 5.4,
        },
    ],
    (37.4530, -122.1826): [
        {"station_id": "KPAO", "name": "Palo Alto Airport Station", "distance": 2.0},
    ],
    (37.4419, -122.1430): [
        {"station_id": "PAO1", "name": "Palo Alto North Station", "distance": 1.5},
    ],
    (21.3069, -157.8583): [
        {"station_id": "PHNL", "name": "Honolulu Station", "distance": 1.0},
    ],
    (19.8968, -155.5828): [
        {"station_id": "PHKO", "name": "Kona Station", "distance": 5.5},
    ],
    (42.6526, -73.7562): [
        {"station_id": "KALB", "name": "Albany Station", "distance": 1.0},
    ],
    (52.5200, 13.4050): [
        {"station_id": "EDDB", "name": "Berlin Brandenburg Airport", "distance": 18.0},
    ],
    (51.5072, -0.1276): [
        {"station_id": "EGLL", "name": "London Heathrow Airport", "distance": 24.0},
    ],
    (50.4504, 30.5245): [
        {
            "station_id": "UKBB",
            "name": "Kyiv Boryspil International Airport",
            "distance": 29.0,
        },
    ],
    (35.6762, 139.6503): [
        {"station_id": "RJTT", "name": "Tokyo Haneda Airport", "distance": 15.0}
    ],
}

# Mock database of timezone information
TIMEZONE_DB = {
    (30.2672, -97.7431): "America/Chicago",
    (30.2021, -97.6686): "America/Chicago",
    (40.7128, -74.0060): "America/New_York",
    (37.7749, -122.4194): "America/Los_Angeles",
    (37.4530, -122.1826): "America/Los_Angeles",
    (37.4419, -122.1430): "America/Los_Angeles",
    (21.3069, -157.8583): "Pacific/Honolulu",
    (19.8968, -155.5828): "Pacific/Honolulu",
    (42.6526, -73.7562): "America/New_York",
    (52.5200, 13.4050): "Europe/Berlin",
    (51.5072, 0.1276): "Europe/London",
    (50.4504, 30.5245): "Europe/Kiev",
    (35.6762, 139.6503): "Asia/Tokyo",
}


# Mock database of hourly observations
TODAY_DATE = datetime.utcnow().strftime("%Y-%m-%d")
HOURLY_OBSERVATIONS = {
    "KATT": {  # Austin Station
        "Monday": [
            "Sunny",
            "Cloudy",
            "Light Rain",
            "Windy",
            "Clear",
            "Thunderstorm",
            "Drizzle",
            "Foggy",
        ],
        "Tuesday": [
            "Partly Cloudy",
            "Sunny",
            "Windy",
            "Rainy",
            "Clear",
            "Overcast",
            "Hazy",
            "Sunny",
        ],
        "Wednesday": [
            "Sunny",
            "Clear",
            "Windy",
            "Foggy",
            "Light Rain",
            "Cloudy",
            "Thunderstorm",
            "Clear",
        ],
        "Thursday": [
            "Clear",
            "Sunny",
            "Cloudy",
            "Stormy",
            "Clear",
            "Drizzle",
            "Windy",
            "Foggy",
        ],
        "Friday": [
            "Windy",
            "Rainy",
            "Sunny",
            "Cloudy",
            "Clear",
            "Thunderstorm",
            "Light Rain",
            "Overcast",
        ],
        "Saturday": [
            "Sunny",
            "Windy",
            "Clear",
            "Clear",
            "Cloudy",
            "Rainy",
            "Sunny",
            "Windy",
        ],
        "Sunday": [
            "Clear",
            "Cloudy",
            "Sunny",
            "Windy",
            "Foggy",
            "Light Rain",
            "Sunny",
            "Cloudy",
        ],
    },
    "KPAO": {  # Palo Alto Airport Station
        "Monday": [
            "Sunny",
            "Clear",
            "Windy",
            "Rainy",
            "Cloudy",
            "Foggy",
            "Light Rain",
            "Clear",
        ],
        "Tuesday": [
            "Cloudy",
            "Rainy",
            "Foggy",
            "Clear",
            "Sunny",
            "Windy",
            "Overcast",
            "Clear",
        ],
        "Wednesday": [
            "Sunny",
            "Clear",
            "Windy",
            "Foggy",
            "Light Rain",
            "Drizzle",
            "Cloudy",
            "Clear",
        ],
        "Thursday": [
            "Windy",
            "Foggy",
            "Sunny",
            "Rainy",
            "Clear",
            "Overcast",
            "Light Rain",
            "Windy",
        ],
        "Friday": [
            "Clear",
            "Cloudy",
            "Windy",
            "Sunny",
            "Clear",
            "Rainy",
            "Sunny",
            "Cloudy",
        ],
        "Saturday": [
            "Rainy",
            "Windy",
            "Cloudy",
            "Sunny",
            "Foggy",
            "Clear",
            "Light Rain",
            "Windy",
        ],
        "Sunday": [
            "Sunny",
            "Clear",
            "Cloudy",
            "Windy",
            "Overcast",
            "Rainy",
            "Clear",
            "Sunny",
        ],
    },
    "KNYC": {  # New York Central Station
        "Monday": [
            "Snowy",
            "Cloudy",
            "Cold",
            "Windy",
            "Clear",
            "Overcast",
            "Light Snow",
            "Foggy",
        ],
        "Tuesday": [
            "Sunny",
            "Clear",
            "Windy",
            "Stormy",
            "Cloudy",
            "Light Snow",
            "Overcast",
            "Clear",
        ],
        "Wednesday": [
            "Rainy",
            "Windy",
            "Cloudy",
            "Sunny",
            "Foggy",
            "Light Snow",
            "Clear",
            "Overcast",
        ],
        "Thursday": [
            "Snowy",
            "Foggy",
            "Cloudy",
            "Windy",
            "Light Snow",
            "Overcast",
            "Clear",
            "Windy",
        ],
        "Friday": [
            "Clear",
            "Sunny",
            "Cold",
            "Windy",
            "Snowy",
            "Cloudy",
            "Foggy",
            "Overcast",
        ],
        "Saturday": [
            "Sunny",
            "Windy",
            "Cloudy",
            "Clear",
            "Light Snow",
            "Foggy",
            "Snowy",
            "Cloudy",
        ],
        "Sunday": [
            "Clear",
            "Snowy",
            "Cold",
            "Windy",
            "Cloudy",
            "Light Snow",
            "Clear",
            "Overcast",
        ],
    },
    "KSFO": {  # San Francisco Airport Station
        "Monday": [
            "Foggy",
            "Cloudy",
            "Sunny",
            "Windy",
            "Clear",
            "Overcast",
            "Light Rain",
            "Foggy",
        ],
        "Tuesday": [
            "Clear",
            "Sunny",
            "Windy",
            "Rainy",
            "Cloudy",
            "Foggy",
            "Overcast",
            "Clear",
        ],
        "Wednesday": [
            "Foggy",
            "Clear",
            "Windy",
            "Sunny",
            "Light Rain",
            "Drizzle",
            "Cloudy",
            "Clear",
        ],
        "Thursday": [
            "Windy",
            "Foggy",
            "Sunny",
            "Rainy",
            "Clear",
            "Overcast",
            "Light Rain",
            "Windy",
        ],
        "Friday": [
            "Clear",
            "Cloudy",
            "Windy",
            "Sunny",
            "Foggy",
            "Rainy",
            "Sunny",
            "Cloudy",
        ],
        "Saturday": [
            "Rainy",
            "Windy",
            "Cloudy",
            "Sunny",
            "Foggy",
            "Clear",
            "Light Rain",
            "Windy",
        ],
        "Sunday": [
            "Sunny",
            "Clear",
            "Cloudy",
            "Windy",
            "Overcast",
            "Rainy",
            "Clear",
            "Sunny",
        ],
    },
    "PHNL": {  # Honolulu Station
        "Monday": [
            "Sunny",
            "Clear",
            "Windy",
            "Rainy",
            "Cloudy",
            "Overcast",
            "Light Rain",
            "Clear",
        ],
        "Tuesday": [
            "Cloudy",
            "Sunny",
            "Windy",
            "Clear",
            "Light Rain",
            "Foggy",
            "Overcast",
            "Clear",
        ],
        "Wednesday": [
            "Sunny",
            "Clear",
            "Windy",
            "Rainy",
            "Cloudy",
            "Light Rain",
            "Overcast",
            "Clear",
        ],
        "Thursday": [
            "Clear",
            "Sunny",
            "Cloudy",
            "Rainy",
            "Windy",
            "Foggy",
            "Light Rain",
            "Sunny",
        ],
        "Friday": [
            "Windy",
            "Rainy",
            "Sunny",
            "Clear",
            "Cloudy",
            "Overcast",
            "Light Rain",
            "Sunny",
        ],
        "Saturday": [
            "Sunny",
            "Windy",
            "Clear",
            "Cloudy",
            "Rainy",
            "Overcast",
            "Sunny",
            "Windy",
        ],
        "Sunday": [
            "Clear",
            "Cloudy",
            "Sunny",
            "Windy",
            "Overcast",
            "Rainy",
            "Clear",
            "Sunny",
        ],
    },
    "PHKO": {  # Kona Station
        "Monday": [
            "Sunny",
            "Windy",
            "Clear",
            "Rainy",
            "Overcast",
            "Foggy",
            "Light Rain",
            "Sunny",
        ],
        "Tuesday": [
            "Clear",
            "Sunny",
            "Windy",
            "Cloudy",
            "Light Rain",
            "Overcast",
            "Clear",
            "Windy",
        ],
        "Wednesday": [
            "Sunny",
            "Clear",
            "Windy",
            "Rainy",
            "Cloudy",
            "Foggy",
            "Overcast",
            "Clear",
        ],
        "Thursday": [
            "Windy",
            "Foggy",
            "Sunny",
            "Rainy",
            "Clear",
            "Overcast",
            "Light Rain",
            "Windy",
        ],
        "Friday": [
            "Clear",
            "Cloudy",
            "Windy",
            "Sunny",
            "Light Rain",
            "Foggy",
            "Overcast",
            "Clear",
        ],
        "Saturday": [
            "Rainy",
            "Windy",
            "Cloudy",
            "Sunny",
            "Foggy",
            "Clear",
            "Light Rain",
            "Windy",
        ],
        "Sunday": [
            "Sunny",
            "Clear",
            "Cloudy",
            "Windy",
            "Overcast",
            "Rainy",
            "Clear",
            "Sunny",
        ],
    },
    "KALB": {  # Albany Station
        "Monday": [
            "Snowy",
            "Cloudy",
            "Cold",
            "Windy",
            "Clear",
            "Overcast",
            "Light Snow",
            "Foggy",
        ],
        "Tuesday": [
            "Clear",
            "Snowy",
            "Cold",
            "Windy",
            "Cloudy",
            "Light Snow",
            "Overcast",
            "Clear",
        ],
        "Wednesday": [
            "Snowy",
            "Windy",
            "Cloudy",
            "Sunny",
            "Foggy",
            "Light Snow",
            "Clear",
            "Overcast",
        ],
        "Thursday": [
            "Clear",
            "Sunny",
            "Cold",
            "Windy",
            "Snowy",
            "Cloudy",
            "Foggy",
            "Overcast",
        ],
        "Friday": [
            "Sunny",
            "Windy",
            "Cloudy",
            "Clear",
            "Light Snow",
            "Foggy",
            "Snowy",
            "Cloudy",
        ],
        "Saturday": [
            "Clear",
            "Snowy",
            "Cold",
            "Windy",
            "Cloudy",
            "Light Snow",
            "Clear",
            "Overcast",
        ],
        "Sunday": [
            "Clear",
            "Cloudy",
            "Sunny",
            "Windy",
            "Overcast",
            "Light Snow",
            "Clear",
            "Sunny",
        ],
    },
    "EDDB": {  # Berlin Brandenburg Airport
        "Monday": [
            "Rainy",
            "Overcast",
            "Windy",
            "Foggy",
            "Clear",
            "Light Rain",
            "Cloudy",
            "Sunny",
        ],
        "Tuesday": [
            "Clear",
            "Rainy",
            "Windy",
            "Foggy",
            "Cloudy",
            "Light Rain",
            "Sunny",
            "Clear",
        ],
        "Wednesday": [
            "Rainy",
            "Windy",
            "Foggy",
            "Overcast",
            "Light Rain",
            "Clear",
            "Sunny",
            "Cloudy",
        ],
        "Thursday": [
            "Clear",
            "Sunny",
            "Cloudy",
            "Rainy",
            "Overcast",
            "Foggy",
            "Light Rain",
            "Windy",
        ],
        "Friday": [
            "Windy",
            "Foggy",
            "Sunny",
            "Rainy",
            "Clear",
            "Overcast",
            "Light Rain",
            "Sunny",
        ],
        "Saturday": [
            "Sunny",
            "Windy",
            "Cloudy",
            "Clear",
            "Rainy",
            "Foggy",
            "Light Rain",
            "Overcast",
        ],
        "Sunday": [
            "Clear",
            "Cloudy",
            "Sunny",
            "Windy",
            "Foggy",
            "Rainy",
            "Overcast",
            "Clear",
        ],
    },
    "EGLL": {  # London Heathrow Airport
        "Monday": [
            "Cloudy",
            "Rainy",
            "Clear",
            "Windy",
            "Overcast",
            "Foggy",
            "Light Rain",
            "Sunny",
        ],
        "Tuesday": [
            "Clear",
            "Cloudy",
            "Windy",
            "Foggy",
            "Rainy",
            "Overcast",
            "Light Rain",
            "Clear",
        ],
        "Wednesday": [
            "Cloudy",
            "Windy",
            "Foggy",
            "Overcast",
            "Light Rain",
            "Clear",
            "Sunny",
            "Rainy",
        ],
        "Thursday": [
            "Clear",
            "Sunny",
            "Cloudy",
            "Rainy",
            "Overcast",
            "Foggy",
            "Light Rain",
            "Windy",
        ],
        "Friday": [
            "Windy",
            "Foggy",
            "Sunny",
            "Rainy",
            "Clear",
            "Overcast",
            "Light Rain",
            "Sunny",
        ],
        "Saturday": [
            "Sunny",
            "Windy",
            "Cloudy",
            "Clear",
            "Rainy",
            "Foggy",
            "Light Rain",
            "Overcast",
        ],
        "Sunday": [
            "Clear",
            "Cloudy",
            "Sunny",
            "Windy",
            "Foggy",
            "Rainy",
            "Overcast",
            "Clear",
        ],
    },
    "UKBB": {  # Kyiv Boryspil International Airport
        "Monday": [
            "Clear",
            "Sunny",
            "Cloudy",
            "Windy",
            "Overcast",
            "Foggy",
            "Light Rain",
            "Sunny",
        ],
        "Tuesday": [
            "Rainy",
            "Clear",
            "Windy",
            "Foggy",
            "Cloudy",
            "Overcast",
            "Light Rain",
            "Clear",
        ],
        "Wednesday": [
            "Sunny",
            "Windy",
            "Foggy",
            "Overcast",
            "Light Rain",
            "Clear",
            "Cloudy",
            "Sunny",
        ],
        "Thursday": [
            "Clear",
            "Sunny",
            "Cloudy",
            "Rainy",
            "Overcast",
            "Foggy",
            "Light Rain",
            "Windy",
        ],
        "Friday": [
            "Windy",
            "Foggy",
            "Sunny",
            "Rainy",
            "Clear",
            "Overcast",
            "Light Rain",
            "Sunny",
        ],
        "Saturday": [
            "Sunny",
            "Windy",
            "Cloudy",
            "Clear",
            "Rainy",
            "Foggy",
            "Light Rain",
            "Overcast",
        ],
        "Sunday": [
            "Clear",
            "Cloudy",
            "Sunny",
            "Windy",
            "Foggy",
            "Rainy",
            "Overcast",
            "Clear",
        ],
    },
    "PAO1": {  # Palo Alto North Station
        "Monday": [
            "Foggy",
            "Cloudy",
            "Clear",
            "Windy",
            "Sunny",
            "Overcast",
            "Light Rain",
            "Clear",
        ],
        "Tuesday": [
            "Clear",
            "Foggy",
            "Windy",
            "Rainy",
            "Cloudy",
            "Overcast",
            "Sunny",
            "Clear",
        ],
        "Wednesday": [
            "Foggy",
            "Clear",
            "Windy",
            "Sunny",
            "Light Rain",
            "Drizzle",
            "Cloudy",
            "Clear",
        ],
        "Thursday": [
            "Windy",
            "Foggy",
            "Sunny",
            "Rainy",
            "Clear",
            "Overcast",
            "Light Rain",
            "Windy",
        ],
        "Friday": [
            "Clear",
            "Cloudy",
            "Windy",
            "Sunny",
            "Foggy",
            "Rainy",
            "Sunny",
            "Cloudy",
        ],
        "Saturday": [
            "Rainy",
            "Windy",
            "Cloudy",
            "Sunny",
            "Foggy",
            "Clear",
            "Light Rain",
            "Windy",
        ],
        "Sunday": [
            "Sunny",
            "Clear",
            "Cloudy",
            "Windy",
            "Overcast",
            "Rainy",
            "Clear",
            "Sunny",
        ],
    },
    "RJTT": {  # Tokyo Haneda Airport
        "Monday": [
            "Sunny",
            "Cloudy",
            "Light Rain",
            "Windy",
            "Clear",
            "Overcast",
            "Drizzle",
            "Foggy",
        ],
        "Tuesday": [
            "Partly Cloudy",
            "Sunny",
            "Windy",
            "Rainy",
            "Clear",
            "Overcast",
            "Hazy",
            "Sunny",
        ],
        "Wednesday": [
            "Rainy",
            "Clear",
            "Windy",
            "Foggy",
            "Light Rain",
            "Cloudy",
            "Thunderstorm",
            "Clear",
        ],
        "Thursday": [
            "Clear",
            "Sunny",
            "Cloudy",
            "Stormy",
            "Clear",
            "Drizzle",
            "Windy",
            "Foggy",
        ],
        "Friday": [
            "Windy",
            "Rainy",
            "Sunny",
            "Cloudy",
            "Clear",
            "Thunderstorm",
            "Light Rain",
            "Overcast",
        ],
        "Saturday": [
            "Sunny",
            "Windy",
            "Clear",
            "Clear",
            "Cloudy",
            "Rainy",
            "Sunny",
            "Windy",
        ],
        "Sunday": [
            "Clear",
            "Cloudy",
            "Sunny",
            "Windy",
            "Foggy",
            "Light Rain",
            "Sunny",
            "Cloudy",
        ],
    },
}

# Current location simulation
CURRENT_LOCATION = "London"


def _similarity_search(data: List[Dict], query: str, key: str) -> List[Dict]:
    """Helper function that returns a list of data that matches the given query using a similarity score. Don't use this function."""

    def _score_function(x: str) -> float:
        """Calculate the similarity score between the query and the given string."""
        return len(set(x.lower()) & set(query.lower())) / len(
            set(x.lower()) | set(query.lower())
        )

    re_ranked_data = sorted(data, key=lambda x: _score_function(x[key]), reverse=True)
    return re_ranked_data


def _similarity_search_list(data: List[Dict], query: list, key: str) -> List[Dict]:
    """Helper function that returns a list of data that matches the given query using a similarity score for list. Don't use this function."""

    def _score_function(x: list) -> float:
        """Calculate the similarity score between the query list and the given list."""
        return 1 - (abs(x[0] - query[0]) + abs(x[1] - query[1])) / 2

    re_ranked_data = sorted(data, key=lambda x: _score_function(x[key]), reverse=True)
    return re_ranked_data


def get_latitude_longitude(location: str) -> list:
    """Retrieve the latitude and longitude of a location, with similarity search if exact match is not found."""
    if location in LOCATION_DB:
        return LOCATION_DB[location]
    else:
        similar_locations = _similarity_search(
            [{"name": name, "coords": coords} for name, coords in LOCATION_DB.items()],
            location,
            "name",
        )
        if similar_locations:
            return similar_locations[0]["coords"]
        return [51.5072, 0.1276]


def get_current_location() -> str:
    """Returns the current location."""
    return CURRENT_LOCATION


def find_nearby_stations(lat_long: list) -> List[Dict]:
    """Provides a list of nearby weather stations for a given geographical location, with similarity search."""
    if not lat_long:
        return []
    lat_long = tuple(lat_long)
    if lat_long in STATIONS_DB:
        return STATIONS_DB[lat_long]
    else:
        similar_locations = _similarity_search_list(
            [{"coords": coords} for coords in STATIONS_DB.keys()], lat_long, "coords"
        )
        if similar_locations:
            return STATIONS_DB[similar_locations[0]["coords"]]
        return []


def get_nearest_station_id(nearby_stations: List[dict]) -> str:
    """Returns the station_id for the nearest station in the list of stations provided."""
    if not nearby_stations:
        return None
    nearest_station = min(nearby_stations, key=lambda x: x["distance"])
    return nearest_station["station_id"]


def get_timezone(lat_long: list) -> str:
    """Gets the timezone for a given latlong, with similarity search."""
    lat_long = tuple(lat_long)
    if lat_long in TIMEZONE_DB:
        return TIMEZONE_DB[lat_long]
    else:
        similar_locations = _similarity_search_list(
            [{"coords": coords} for coords in TIMEZONE_DB.keys()], lat_long, "coords"
        )
        if similar_locations:
            return TIMEZONE_DB[similar_locations[0]["coords"]]
        return "UTC"


def get_hourly_observation(
    station_id: str, start_time: str, end_time: str, time_zone: str
) -> List[str]:
    """Returns hourly observations between start_time and end_time."""
    start_date = datetime.strptime(start_time.split(" ")[0], "%Y-%m-%d").date()
    end_date = datetime.strptime(end_time.split(" ")[0], "%Y-%m-%d").date()

    observations = []

    for single_date in (
        start_date + timedelta(n) for n in range((end_date - start_date).days + 1)
    ):
        day_of_week = single_date.strftime(
            "%A"
        )  # Get the day of the week (e.g., "Monday")
        daily_observations = HOURLY_OBSERVATIONS.get(station_id, {}).get(
            day_of_week, []
        )
        observations.extend(daily_observations)

    return observations


def subtract_time_delta(date_time_str: str, delta_days: int) -> str:
    """Subtracts a time delta from the date part of a given date time string and returns the new date string."""
    date_part = date_time_str.split(" ")[0]
    date_time = datetime.strptime(date_part, "%Y-%m-%d")
    new_date_time = date_time - timedelta(days=delta_days)
    return new_date_time.strftime("%Y-%m-%d")


def get_current_time_at_location(lat_long: list) -> str:
    """Returns the current time at a given location."""
    timezone = get_timezone(lat_long)
    current_time = datetime.utcnow()
    return current_time.strftime("%Y-%m-%d %H:%M:%S")


get_latitude_longitude_json = {
    "name": "get_latitude_longitude",
    "description": "Given a city name, this function provides the latitude and longitude of the specific location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The name of the location (e.g., 'Austin', 'Austin Airport').",
            }
        },
        "required": ["location"],
    },
    "returns": {
        "type": "array",
        "items": {"type": "number"},
        "description": "A list containing the latitude and longitude of the location.",
    },
}

get_current_location_json = {
    "name": "get_current_location",
    "description": "Returns the current location. ONLY use this if the user has not provided an explicit location in the query.",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": [],
    },
    "returns": {
        "type": "string",
        "description": "The current location as a string (e.g., 'Austin').",
    },
}

find_nearby_stations_json = {
    "name": "find_nearby_stations",
    "description": "This endpoint provides a list of nearby weather stations for a given geographical location.",
    "parameters": {
        "type": "object",
        "properties": {
            "lat_long": {
                "type": "array",
                "items": {"type": "number"},
                "description": "A list containing the latitude and longitude.",
            }
        },
        "required": ["lat_long"],
    },
    "returns": {
        "type": "array",
        "items": {"type": "object"},
        "description": "A list of dictionaries about the various stations near the specified location.",
    },
}

get_nearest_station_id_json = {
    "name": "get_nearest_station_id",
    "description": "Given a list of nearby stations, returns the one nearest to you and provides the system ID for it alone.",
    "parameters": {
        "type": "object",
        "properties": {
            "nearby_stations": {
                "type": "array",
                "items": {"type": "object"},
                "description": "A list of nearby stations in dictionary format.",
            }
        },
        "required": ["nearby_stations"],
    },
    "returns": {
        "type": "string",
        "description": "The station_id for the nearest station in the list.",
    },
}

get_timezone_json = {
    "name": "get_timezone",
    "description": "This function retrieves the timezone for a given latitude and longitude.",
    "parameters": {
        "type": "object",
        "properties": {
            "lat_long": {
                "type": "array",
                "items": {"type": "number"},
                "description": "The latitude and longitude of the area.",
            }
        },
        "required": ["lat_long"],
    },
    "returns": {
        "type": "string",
        "description": "The timezone string ID for the specified location.",
    },
}

get_hourly_observation_json = {
    "name": "get_hourly_observation",
    "description": "Returns hourly observations between start_time and end_time.",
    "parameters": {
        "type": "object",
        "properties": {
            "station_id": {
                "type": "string",
                "description": "The station_id for the station of interest.",
            },
            "start_time": {
                "type": "string",
                "description": "The start time in 'YYYY-MM-DD' format.",
            },
            "end_time": {
                "type": "string",
                "description": "The end time in 'YYYY-MM-DD' format.",
            },
            "time_zone": {
                "type": "string",
                "description": "The timezone string ID for the location.",
            },
        },
        "required": ["station_id", "start_time", "end_time", "time_zone"],
    },
    "returns": {
        "type": "array",
        "items": {"type": "object"},
        "description": "A list of hourly observations for the specified station and timespan.",
    },
}

subtract_time_delta_json = {
    "name": "subtract_time_delta",
    "description": "Subtracts a time delta from the date part of a given date time string and returns the new date string.",
    "parameters": {
        "type": "object",
        "properties": {
            "date_time_str": {
                "type": "string",
                "description": "The date time string in 'YYYY-MM-DD' format.",
            },
            "delta_days": {
                "type": "integer",
                "description": "Number of days to subtract. Must be greater than 0.",
            },
        },
        "required": ["date_time_str", "delta_days"],
    },
    "returns": {
        "type": "string",
        "description": "The new date string after subtracting the delta.",
    },
}

get_current_time_at_location_json = {
    "name": "get_current_time_at_location",
    "description": "Returns the current time at a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "lat_long": {
                "type": "array",
                "items": {"type": "number"},
                "description": "The latitude and longitude of the location.",
            }
        },
        "required": ["lat_long"],
    },
    "returns": {
        "type": "string",
        "description": "The current time at the specified location.",
    },
}
