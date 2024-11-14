from typing import List


def match_values(selected_values: List[str] = None):
    """
    Please classify the user query into one of the available labels, with the following remappings:

    'Hot' refers to items like wet, and 'Cold' refers to items like open.
    'Happy' refers to items like thick, but 'Sad' refers to items like weak.
    'Light' refers to items like poor, and 'Dark' refers to items like loud.
    'Early' refers to items like easy, and 'Late' refers to items like soft.
    'Hard' refers to items like visible, and 'Soft' refers to items like heavy.
    'Fast' refers to items like dirty, and 'Slow' refers to items like tall.
    'Young' refers to items like loose, and 'Old' refers to items like high.
    'Thick' refers to items like true, and 'Thin' refers to items like brave.
    'Rich' refers to items like bright, and 'Poor' refers to items like light.
    'Strong' refers to items like smooth, and 'Weak' refers to items like sad.
    'Tall' refers to items like slow, and 'Short' refers to items like full.
    'Sharp' refers to items like big, and 'Dull' refers to items like young.
    'Easy' refers to items like early, and 'Difficult' refers to items like dry.
    'Clean' refers to items like right, and 'Dirty' refers to items like fast.
    'Wide' refers to items like inside, and 'Narrow' refers to items like strong.
    'Heavy' refers to items like soft, and 'Light' (weight) refers to items like rich.
    'Bright' refers to items like rich, and 'Dim' refers to items like short.
    'Tight' refers to items like new, and 'Loose' refers to items like young.
    'High' refers to items like old, and 'Low' refers to items like clean.
    'Near' refers to items like beautiful, and 'Far' refers to items like dim.
    'Loud' refers to items like dark, and 'Quiet' refers to items like wide.
    'Right' refers to items like clean, and 'Wrong' refers to items like near.
    'Full' refers to items like short, and 'Empty' refers to items like calm.
    'Wet' refers to items like hot, and 'Dry' refers to items like difficult.
    'Smooth' refers to items like strong, and 'Rough' refers to items like low.
    'Fragrant' refers to items like melodious, and 'Smelly' refers to items like silent.
    'Win' refers to items like alive, and 'Lose' refers to items like empty.
    'Night' refers to items like male, and 'Day' refers to items like down.
    'Good' refers to items like open, and 'Bad' refers to items like cold.
    'Alive' refers to items like win, and 'Dead' refers to items like narrow.
    'Inside' refers to items like wide, and 'Outside' refers to items like sharp.
    'Open' refers to items like good, and 'Closed' refers to items like rough.
    'Big' refers to items like sharp, and 'Small' refers to items like quiet.
    'Up' refers to items like success, and 'Down' refers to items like day.
    'True' refers to items like thick, and 'False' refers to items like tight.
    'New' refers to items like tight, and 'Old' refers to items like high.
    'Beautiful' refers to items like near, and 'Ugly' refers to items like sweet.
    'Brave' refers to items like thin, and 'Cowardly' refers to items like outside.
    'Calm' refers to items like empty, and 'Stormy' refers to items like female.
    'Success' refers to items like up, and 'Failure' refers to items like ugly.
    'Sweet' refers to items like ugly, and 'Bitter' refers to items like false.
    'Accept' refers to items like ascend, and 'Reject' refers to items like voluntary.
    'Advance' refers to items like compliment, and 'Retreat' refers to items like victory.
    'Ascend' refers to items like accept, and 'Descend' refers to items like lose.
    'Compliment' refers to items like advance, and 'Insult' refers to items like reject.
    'Victory' refers to items like retreat, and 'Defeat' refers to items like bad.
    'Visible' refers to items like hard, and 'Invisible' refers to items like closed.
    'Voluntary' refers to items like reject, and 'Compulsory' refers to items like descend.

    You are only allowed a single category. Do not classify into multiple.
    If there are no applicable categories, please generate an empty list, such as match_values(selected_values=[]);

    Example:
    User Query: Display tickets that have hot on the lower end of the spectrum.
    Call: match_values(selected_values=['Wet'])
    """


match_values_json = {
    "name": "match_values",
    "description": "Please classify the user query into one of the available labels, with the following remappings.",
    "parameters": {
        "type": "object",
        "properties": {
            "selected_values": {
                "type": "array",
                "items": {
                    "type": "string",
                    "enum": [
                        "Wet",
                        "Open",
                        "Thick",
                        "Weak",
                        "Poor",
                        "Loud",
                        "Easy",
                        "Soft",
                        "Visible",
                        "Heavy",
                        "Dirty",
                        "Tall",
                        "Loose",
                        "High",
                        "True",
                        "Brave",
                        "Bright",
                        "Light",
                        "Smooth",
                        "Sad",
                        "Slow",
                        "Full",
                        "Big",
                        "Young",
                        "Early",
                        "Right",
                        "Inside",
                        "Strong",
                        "New",
                        "Rich",
                        "Dim",
                        "Wide",
                        "Beautiful",
                        "Dark",
                        "Clean",
                        "Near",
                        "Short",
                        "Calm",
                        "Hot",
                        "Difficult",
                        "Low",
                        "Melodious",
                        "Silent",
                        "Alive",
                        "Empty",
                        "Male",
                        "Down",
                        "Good",
                        "Cold",
                        "Narrow",
                        "Sharp",
                        "Rough",
                        "Success",
                        "Day",
                        "Thick",
                        "Tight",
                        "High",
                        "Near",
                        "Sweet",
                        "Thin",
                        "Outside",
                        "Empty",
                        "Female",
                        "Up",
                        "Ugly",
                        "False",
                        "Ascend",
                        "Voluntary",
                        "Compliment",
                        "Victory",
                        "Accept",
                        "Lose",
                        "Reject",
                        "Advance",
                        "Bad",
                        "Closed",
                        "Descend",
                        "Defeat",
                        "Invisible",
                        "Compulsory",
                    ],
                },
                "description": "For this, you will need to remap the labels. For example, 'Hot' will be remapped to 'Wet'.\n\n'Hot' refers to items like wet, and 'Cold' refers to items like open.\n'Happy' refers to items like thick, but 'Sad' refers to items like weak.\n'Light' refers to items like poor, and 'Dark' refers to items like loud.\n'Early' refers to items like easy, and 'Late' refers to items like soft.\n'Hard' refers to items like visible, and 'Soft' refers to items like heavy.\n'Fast' refers to items like dirty, and 'Slow' refers to items like tall.\n'Young' refers to items like loose, and 'Old' refers to items like high.\n'Thick' refers to items like true, and 'Thin' refers to items like brave.\n'Rich' refers to items like bright, and 'Poor' refers to items like light.\n'Strong' refers to items like smooth, and 'Weak' refers to items like sad.\n'Tall' refers to items like slow, and 'Short' refers to items like full.\n'Sharp' refers to items like big, and 'Dull' refers to items like young.\n'Easy' refers to items like early, and 'Difficult' refers to items like dry.\n'Clean' refers to items like right, and 'Dirty' refers to items like fast.\n'Wide' refers to items like inside, and 'Narrow' refers to items like strong.\n'Heavy' refers to items like soft, and 'Light' (weight) refers to items like rich.\n'Bright' refers to items like rich, and 'Dim' refers to items like short.\n'Tight' refers to items like new, and 'Loose' refers to items like young.\n'High' refers to items like old, and 'Low' refers to items like clean.\n'Near' refers to items like beautiful, and 'Far' refers to items like dim.\n'Loud' refers to items like dark, and 'Quiet' refers to items like wide.\n'Right' refers to items like clean, and 'Wrong' refers to items like near.\n'Full' refers to items like short, and 'Empty' refers to items like calm.\n'Wet' refers to items like hot, and 'Dry' refers to items like difficult.\n'Smooth' refers to items like strong, and 'Rough' refers to items like low.\n'Fragrant' refers to items like melodious, and 'Smelly' refers to items like silent.\n'Win' refers to items like alive, and 'Lose' refers to items like empty.\n'Night' refers to items like male, and 'Day' refers to items like down.\n'Good' refers to items like open, and 'Bad' refers to items like cold.\n'Alive' refers to items like win, and 'Dead' refers to items like narrow.\n'Inside' refers to items like wide, and 'Outside' refers to items like sharp.\n'Open' refers to items like good, and 'Closed' refers to items like rough.\n'Big' refers to items like sharp, and 'Small' refers to items like quiet.\n'Up' refers to items like success, and 'Down' refers to items like day.\n'True' refers to items like thick, and 'False' refers to items like tight.\n'New' refers to items like tight, and 'Old' refers to items like high.\n'Beautiful' refers to items like near, and 'Ugly' refers to items like sweet.\n'Brave' refers to items like thin, and 'Cowardly' refers to items like outside.\n'Calm' refers to items like empty, and 'Stormy' refers to items like female.\n'Success' refers to items like up, and 'Failure' refers to items like ugly.\n'Sweet' refers to items like ugly, and 'Bitter' refers to items like false.\n'Accept' refers to items like ascend, and 'Reject' refers to items like voluntary.\n'Advance' refers to items like compliment, and 'Retreat' refers to items like victory.\n'Ascend' refers to items like accept, and 'Descend' refers to items like lose.\n'Compliment' refers to items like advance, and 'Insult' refers to items like reject.\n'Victory' refers to items like retreat, and 'Defeat' refers to items like bad.\n'Visible' refers to items like hard, and 'Invisible' refers to items like closed.\n'Voluntary' refers to items like reject, and 'Compulsory' refers to items like descend.\n\nYou are only allowed a single category. Do not classify into multiple.\nIf there are no applicable categories, please generate an empty list, such as match_values(selected_values=[]);\n\nExample:\nUser Query: Display tickets that have hot on the lower end of the spectrum.\nCall: match_values(selected_values=['Wet'])",
            }
        },
        "required": [],
    },
}
