from typing import List, Optional

USER_DATA = [
    {
        "id": 1,
        "name": "Alice",
        "email": "alice@gmail.com",
        "location": 1,
        "favorite_color": "red",
        "favorite_foods": [1, 2, 3],
    },
    {
        "id": 21,
        "name": "Bob",
        "email": "bob@hotmail.com",
        "location": 2,
        "favorite_color": "orange",
        "favorite_foods": [4, 5, 6],
    },
    {
        "id": 35,
        "name": "Charlie",
        "email": "charlie@yahoo.com",
        "location": 3,
        "favorite_color": "yellow",
        "favorite_foods": [3, 7, 2],
    },
    {
        "id": 41,
        "name": "Donna",
        "email": "donna@example.com",
        "location": 4,
        "favorite_color": "green",
        "favorite_foods": [6, 1, 4],
    },
    {
        "id": 42,
        "name": "Eve",
        "email": "eve@example.org",
        "location": 5,
        "favorite_color": "blue",
        "favorite_foods": [5, 7, 4],
    },
    {
        "id": 43,
        "name": "Frank",
        "email": "frank.the.cat@langchain.dev",
        "location": 5,
        "favorite_color": "yellow",
        "favorite_foods": [3],
    },
]

LOCATION_DATA = [
    {
        "id": 1,
        "city": "New York",
        "current_time": "2023-11-14 10:30 AM",
        "current_weather": "Partly Cloudy, Temperature: 68°F",  # Example weather string
    },
    {
        "id": 2,
        "city": "Los Angeles",
        "current_time": "2023-11-14 7:45 AM",
        "current_weather": "Sunny, Temperature: 75°F",  # Example weather string
    },
    {
        "id": 3,
        "city": "Chicago",
        "current_time": "2023-11-14 11:15 AM",
        "current_weather": "Mostly Cloudy, Temperature: 60°F",  # Example weather string
    },
    {
        "id": 4,
        "city": "Houston",
        "current_time": "2023-11-14 12:00 PM",
        "current_weather": "Rainy, Temperature: 55°F",  # Example weather string
    },
    {
        "id": 5,
        "city": "Miami",
        "current_time": "2023-11-14 1:20 PM",
        "current_weather": "Partly Cloudy, Temperature: 80°F",  # Example weather string
    },
]

FOOD_DATA = [
    {
        "id": 1,
        "name": "Pizza",
        "calories": 285,  # Calories per serving
        "allergic_ingredients": ["Gluten", "Dairy"],
    },
    {
        "id": 2,
        "name": "Chocolate",
        "calories": 50,  # Calories per serving
        "allergic_ingredients": ["Milk", "Soy"],
    },
    {
        "id": 3,
        "name": "Sushi",
        "calories": 300,  # Calories per serving
        "allergic_ingredients": ["Fish", "Soy"],
    },
    {
        "id": 4,
        "name": "Burger",
        "calories": 350,  # Calories per serving
        "allergic_ingredients": ["Gluten", "Dairy"],
    },
    {
        "id": 5,
        "name": "Ice Cream",
        "calories": 200,  # Calories per serving
        "allergic_ingredients": ["Dairy"],
    },
    {
        "id": 6,
        "name": "Pasta",
        "calories": 180,  # Calories per serving
        "allergic_ingredients": ["Gluten"],
    },
    {
        "id": 7,
        "name": "Salad",
        "calories": 50,  # Calories per serving
        "allergic_ingredients": [],
    },
]


class SearchHit:
    """A search hit."""

    id: Optional[str] = None


def _similarity_search(data: List[dict], query: str, key: str):
    """Return a list of data that matches the given query.

    Similarity score is jaccard similarity based on the number of shared
    characters between the query and the data.

    This is a helper function for other tools, so don't use this directly.

    Args:
        data: The data to search.
        query: The query to search for.
        key: The key to search in.

    Returns:
        The list of matching data.
    """

    def _score_function(x: str) -> float:
        """Calculate the similarity score between the query and the given string."""
        return len(set(x) & set(query)) / len(set(x) | set(query))

    re_ranked_data = sorted(data, key=lambda x: _score_function(x[key]), reverse=True)
    return [{"id": d["id"], key: d[key]} for d in re_ranked_data]


def get_user_info(id: int) -> dict:
    """Find the user with the given user ID.

    Args:
        id: The user's ID.

    Returns:
        The user's data.
    """
    for user in USER_DATA:
        if user["id"] == id:
            return user
    raise Exception(f"User ID {id} cannot be resolved")


def get_location_info(id: int) -> dict:
    """Find the location with the given location ID.

    Args:
        id: The location's ID.

    Returns:
        The location's data.
    """
    for location in LOCATION_DATA:
        if location["id"] == id:
            return location
    raise Exception(f"Location ID {id} cannot be resolved")


def get_food_info(food_id: int) -> dict:
    """Find the food with the given food ID.

    Args:
        food_id: The food's ID.

    Returns:
        The food's data.
    """
    for food in FOOD_DATA:
        if food["id"] == food_id:
            return food
    raise Exception(f"Food ID {food_id} cannot be resolved")


def get_user_name(user_id: int) -> str:
    """Get the name of the user with the given user ID.

    Args:
        user_id: The user's ID.

    Returns:
        The user's name.
    """
    return get_user_info(user_id)["name"]


def list_user_ids() -> List[str]:
    """List all the user IDs."""
    return [user["id"] for user in USER_DATA]


def find_users_by_name(name: str):
    """Find users with the given name.

    Args:
        name: The name to search for.

    Returns:
        The list of matching users.
    """
    return _similarity_search(USER_DATA, name, "name")


def find_locations_by_name(city: str):
    """Find locations with the given city name."""
    return _similarity_search(LOCATION_DATA, city, "city")


def find_foods_by_name(food: str):
    """Find foods with the given name."""
    return _similarity_search(FOOD_DATA, food, "name")


def get_user_email(user_id: int) -> str:
    """Get the email of the user with the given user ID.

    Args:
        user_id: The user's ID.

    Returns:
        The user's email.
    """
    return get_user_info(user_id)["email"]


def get_user_location(user_id: int) -> int:
    """Get the location ID of the user with the given user ID.

    Args:
        user_id: The user's ID.

    Returns:
        The user's location ID.
    """
    return get_user_info(user_id)["location"]


def get_user_favorite_color(user_id: int) -> str:
    """Get the favorite color of the user with the given user ID.

    Args:
        user_id: The user's ID.

    Returns:
        The user's favorite color.
    """
    return get_user_info(user_id)["favorite_color"]


def get_user_favorite_foods(user_id: int) -> List[int]:
    """Get the list of favorite foods of the user with the given user ID.

    Args:
        user_id: The user's ID.

    Returns:
        The list of favorite foods.
    """
    return get_user_info(user_id)["favorite_foods"]


def get_weather_at_location(location_id: int) -> str:
    """Get the current weather at the location with the given location ID.

    Args:
        location_id: The location's ID.

    Returns:
        The current weather at the location.
    """
    return get_location_info(location_id)["current_weather"]


def get_city_for_location(location_id: int) -> str:
    """Get the city for the location with the given location ID.

    Args:
        location_id: The location's ID.

    Returns:
        The city name for the location.
    """
    return get_location_info(location_id)["city"]


def get_current_time_for_location(location_id: int) -> str:
    """Get the current time for the location with the given location ID.

    Args:
        location_id: The location's ID.

    Returns:
        The current time for the location.
    """
    return get_location_info(location_id)["current_time"]


def get_current_weather_for_location(location_id: int) -> str:
    """Get the current weather for the location with the given location ID.

    Args:
        location_id: The location's ID.

    Returns:
        The current weather for the location.
    """
    return get_location_info(location_id)["current_weather"]


def get_food_name(food_id: int) -> str:
    """Get the name of the food with the given food ID.

    Args:
        food_id: The food's ID.

    Returns:
        The name of the food.
    """
    return get_food_info(food_id)["name"]


def get_food_calories(food_id: int) -> int:
    """Get the calories per serving for the food with the given food ID.

    Args:
        food_id: The food's ID.

    Returns:
        The calories per serving of the food.
    """
    return get_food_info(food_id)["calories"]


def get_food_allergic_ingredients(food_id: int) -> List[str]:
    """Get the list of allergic ingredients for the food with the given food ID.

    Args:
        food_id: The food's ID.

    Returns:
        The list of allergic ingredients.
    """
    return get_food_info(food_id)["allergic_ingredients"]


def get_current_user_id() -> int:
    """Get the current user's ID.

    Returns:
        The current user's ID.
    """
    return 35


_similarity_search_json = {
    "name": "_similarity_search",
    "description": "Return a list of data that matches the given query.\n\nSimilarity score is jaccard similarity based on the number of shared characters between the query and the data.\n\nThis is a helper function for other tools, so don't use this directly.",
    "parameters": {
        "type": "object",
        "properties": {
            "data": {
                "type": "array",
                "items": {"type": "object"},
                "description": "The data to search.",
            },
            "query": {"type": "string", "description": "The query to search for."},
            "key": {"type": "string", "description": "The key to search in."},
        },
        "required": ["data", "query", "key"],
    },
    "returns": {
        "type": "array",
        "items": {"type": "object"},
        "description": "The list of matching data.",
    },
}

get_user_info_json = {
    "name": "get_user_info",
    "description": "Find the user with the given user ID.",
    "parameters": {
        "type": "object",
        "properties": {"id": {"type": "integer", "description": "The user's ID."}},
        "required": ["id"],
    },
    "returns": {"type": "object", "description": "The user's data."},
}

get_location_info_json = {
    "name": "get_location_info",
    "description": "Find the location with the given location ID.",
    "parameters": {
        "type": "object",
        "properties": {"id": {"type": "integer", "description": "The location's ID."}},
        "required": ["id"],
    },
    "returns": {"type": "object", "description": "The location's data."},
}

get_food_info_json = {
    "name": "get_food_info",
    "description": "Find the food with the given food ID.",
    "parameters": {
        "type": "object",
        "properties": {"food_id": {"type": "integer", "description": "The food's ID."}},
        "required": ["food_id"],
    },
    "returns": {"type": "object", "description": "The food's data."},
}

get_user_name_json = {
    "name": "get_user_name",
    "description": "Get the name of the user with the given user ID.",
    "parameters": {
        "type": "object",
        "properties": {"user_id": {"type": "integer", "description": "The user's ID."}},
        "required": ["user_id"],
    },
    "returns": {"type": "string", "description": "The user's name."},
}

list_user_ids_json = {
    "name": "list_user_ids",
    "description": "List all the user IDs.",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": [],
    },
    "returns": {
        "type": "array",
        "items": {"type": "string"},
        "description": "The list of user IDs.",
    },
}

find_users_by_name_json = {
    "name": "find_users_by_name",
    "description": "Find users with the given name.",
    "parameters": {
        "type": "object",
        "properties": {
            "name": {"type": "string", "description": "The name to search for."}
        },
        "required": ["name"],
    },
    "returns": {
        "type": "array",
        "items": {"type": "object"},
        "description": "The list of matching users.",
    },
}

find_locations_by_name_json = {
    "name": "find_locations_by_name",
    "description": "Find locations with the given city name.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {"type": "string", "description": "The city name to search for."}
        },
        "required": ["city"],
    },
    "returns": {
        "type": "array",
        "items": {"type": "object"},
        "description": "The list of matching locations.",
    },
}

find_foods_by_name_json = {
    "name": "find_foods_by_name",
    "description": "Find foods with the given name.",
    "parameters": {
        "type": "object",
        "properties": {
            "food": {"type": "string", "description": "The food name to search for."}
        },
        "required": ["food"],
    },
    "returns": {
        "type": "array",
        "items": {"type": "object"},
        "description": "The list of matching foods.",
    },
}

get_user_email_json = {
    "name": "get_user_email",
    "description": "Get the email of the user with the given user ID.",
    "parameters": {
        "type": "object",
        "properties": {"user_id": {"type": "integer", "description": "The user's ID."}},
        "required": ["user_id"],
    },
    "returns": {"type": "string", "description": "The user's email."},
}

get_user_location_json = {
    "name": "get_user_location",
    "description": "Get the location ID of the user with the given user ID.",
    "parameters": {
        "type": "object",
        "properties": {"user_id": {"type": "integer", "description": "The user's ID."}},
        "required": ["user_id"],
    },
    "returns": {"type": "integer", "description": "The user's location ID."},
}

get_user_favorite_color_json = {
    "name": "get_user_favorite_color",
    "description": "Get the favorite color of the user with the given user ID.",
    "parameters": {
        "type": "object",
        "properties": {"user_id": {"type": "integer", "description": "The user's ID."}},
        "required": ["user_id"],
    },
    "returns": {"type": "string", "description": "The user's favorite color."},
}

get_user_favorite_foods_json = {
    "name": "get_user_favorite_foods",
    "description": "Get the list of favorite foods of the user with the given user ID.",
    "parameters": {
        "type": "object",
        "properties": {"user_id": {"type": "integer", "description": "The user's ID."}},
        "required": ["user_id"],
    },
    "returns": {
        "type": "array",
        "items": {"type": "integer"},
        "description": "The list of favorite foods.",
    },
}

get_weather_at_location_json = {
    "name": "get_weather_at_location",
    "description": "Get the current weather at the location with the given location ID.",
    "parameters": {
        "type": "object",
        "properties": {
            "location_id": {"type": "integer", "description": "The location's ID."}
        },
        "required": ["location_id"],
    },
    "returns": {
        "type": "string",
        "description": "The current weather at the location.",
    },
}

get_city_for_location_json = {
    "name": "get_city_for_location",
    "description": "Get the city for the location with the given location ID.",
    "parameters": {
        "type": "object",
        "properties": {
            "location_id": {"type": "integer", "description": "The location's ID."}
        },
        "required": ["location_id"],
    },
    "returns": {"type": "string", "description": "The city name for the location."},
}

get_current_time_for_location_json = {
    "name": "get_current_time_for_location",
    "description": "Get the current time for the location with the given location ID.",
    "parameters": {
        "type": "object",
        "properties": {
            "location_id": {"type": "integer", "description": "The location's ID."}
        },
        "required": ["location_id"],
    },
    "returns": {"type": "string", "description": "The current time for the location."},
}

get_current_weather_for_location_json = {
    "name": "get_current_weather_for_location",
    "description": "Get the current weather for the location with the given location ID.",
    "parameters": {
        "type": "object",
        "properties": {
            "location_id": {"type": "integer", "description": "The location's ID."}
        },
        "required": ["location_id"],
    },
    "returns": {
        "type": "string",
        "description": "The current weather for the location.",
    },
}

get_food_name_json = {
    "name": "get_food_name",
    "description": "Get the name of the food with the given food ID.",
    "parameters": {
        "type": "object",
        "properties": {"food_id": {"type": "integer", "description": "The food's ID."}},
        "required": ["food_id"],
    },
    "returns": {"type": "string", "description": "The name of the food."},
}

get_food_calories_json = {
    "name": "get_food_calories",
    "description": "Get the calories per serving for the food with the given food ID.",
    "parameters": {
        "type": "object",
        "properties": {"food_id": {"type": "integer", "description": "The food's ID."}},
        "required": ["food_id"],
    },
    "returns": {
        "type": "integer",
        "description": "The calories per serving of the food.",
    },
}

get_food_allergic_ingredients_json = {
    "name": "get_food_allergic_ingredients",
    "description": "Get the list of allergic ingredients for the food with the given food ID.",
    "parameters": {
        "type": "object",
        "properties": {"food_id": {"type": "integer", "description": "The food's ID."}},
        "required": ["food_id"],
    },
    "returns": {
        "type": "array",
        "items": {"type": "string"},
        "description": "The list of allergic ingredients.",
    },
}


get_current_user_id_json = {
    "name": "get_current_user_id",
    "description": "Get the current user's ID.",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": [],
    },
    "returns": {"type": "integer", "description": "The current user's ID."},
}
