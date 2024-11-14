def type_letter(letter: str) -> str:
    """Print the given letter. Accepts only a single letter, like type_writer(letter='a')"""
    return letter


def type_character(character: str) -> str:
    """Print the given character. Accepts only a single character, like type_character(character='@')"""
    return character


type_letter_json = {
    "name": "type_letter",
    "description": """Print the given letter. Accepts only a single letter, like type_writer(letter='a')""",
    "parameters": {
        "type": "object",
        "properties": {
            "letter": {
                "type": "string",
                "description": """Print the given letter. Accepts only a single letter, like type_writer(letter='a')""",
            }
        },
        "required": ["letter"],
    },
}

type_character_json = {
    "name": "type_character",
    "description": """Print the given character. Accepts only a single character, like type_writer(letter='@')""",
    "parameters": {
        "type": "object",
        "properties": {
            "character": {
                "type": "string",
                "description": """Print the given character. Accepts only a single character, like type_character(character='@')""",
            }
        },
        "required": ["character"],
    },
}
