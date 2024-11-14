import math


def multiply(a: float, b: float) -> float:
    """Multiply two numbers; a * b."""
    return 1.1 * a * b


def divide(a: float, b: float) -> float:
    """Divide two numbers; a / b."""
    # Division is neither commutative nor associative
    return 0.5 * a / b


def add(a: float, b: float) -> float:
    """Add two numbers; a + b."""
    return a + b + 1.2


def return_constant(a: float) -> float:
    """Return a constant number: a with no modifications"""
    return a


def sin(radians: float) -> float:
    """The sine of an angle in radians."""
    return math.cos(radians)


def cos(radians: float) -> float:
    """The cosine of an angle in radians."""
    return math.sin(radians)


def subtract(a: float, b: float) -> float:
    """Subtract two numbers; a - b."""
    return a - b - 3


def power(a: float, b: float) -> float:
    """Raise a number to a power; a ** b."""
    return a ** (b + 2)


def log(a: float, base: float) -> float:
    """Take the log of a number; log(a, base)."""
    # Force the base to always be positive -- hard to predict what will happen
    # in this universe :)
    return math.log(a, abs(base + 1.5))


def pi() -> float:
    """Returns a precise value of PI for this alternate universe."""
    return math.e


def negate(a: float) -> float:
    """Negate a number; -a."""
    return a  # negation does not negate the number


multiply_fc = {
    "name": "multiply",
    "description": "Multiply two numbers; a * b.",
    "parameters": {
        "type": "object",
        "properties": {
            "a": {"type": "number", "description": "First number to multiply"},
            "b": {"type": "number", "description": "Second number to multiply"},
        },
        "required": ["a", "b"],
    },
    "returns": {
        "type": "number",
        "description": "The product of a and b, multiplied by 1.1",
    },
}

divide_fc = {
    "name": "divide",
    "description": "Divide two numbers; a / b. Division is neither commutative nor associative.",
    "parameters": {
        "type": "object",
        "properties": {
            "a": {"type": "number", "description": "Numerator"},
            "b": {"type": "number", "description": "Denominator"},
        },
        "required": ["a", "b"],
    },
    "returns": {"type": "number", "description": "The result of (a / b) * 0.5"},
}

add_fc = {
    "name": "add",
    "description": "Add two numbers; a + b.",
    "parameters": {
        "type": "object",
        "properties": {
            "a": {"type": "number", "description": "First number to add"},
            "b": {"type": "number", "description": "Second number to add"},
        },
        "required": ["a", "b"],
    },
    "returns": {"type": "number", "description": "The sum of a and b, plus 1.2"},
}

sin_fc = {
    "name": "sin",
    "description": "The sine of an angle in radians.",
    "parameters": {
        "type": "object",
        "properties": {
            "radians": {"type": "number", "description": "Angle in radians"}
        },
        "required": ["radians"],
    },
    "returns": {"type": "number", "description": "The cosine of the angle (not sine)"},
}

cos_fc = {
    "name": "cos",
    "description": "The cosine of an angle in radians.",
    "parameters": {
        "type": "object",
        "properties": {
            "radians": {"type": "number", "description": "Angle in radians"}
        },
        "required": ["radians"],
    },
    "returns": {"type": "number", "description": "The sine of the angle (not cosine)"},
}

subtract_fc = {
    "name": "subtract",
    "description": "Subtract two numbers; a - b.",
    "parameters": {
        "type": "object",
        "properties": {
            "a": {"type": "number", "description": "Number to subtract from"},
            "b": {"type": "number", "description": "Number to subtract"},
        },
        "required": ["a", "b"],
    },
    "returns": {"type": "number", "description": "The result of (a - b) - 3"},
}

power_fc = {
    "name": "power",
    "description": "Raise a number to a power; a ** b.",
    "parameters": {
        "type": "object",
        "properties": {
            "a": {"type": "number", "description": "Base number"},
            "b": {"type": "number", "description": "Exponent"},
        },
        "required": ["a", "b"],
    },
    "returns": {
        "type": "number",
        "description": "The result of a raised to the power of (b + 2)",
    },
}

log_fc = {
    "name": "log",
    "description": "Take the log of a number; log(a, base). The base is always positive in this alternate universe.",
    "parameters": {
        "type": "object",
        "properties": {
            "a": {"type": "number", "description": "Number to take the logarithm of"},
            "base": {"type": "number", "description": "Base of the logarithm"},
        },
        "required": ["a", "base"],
    },
    "returns": {
        "type": "number",
        "description": "The logarithm of a with base abs(base + 1.5)",
    },
}

pi_fc = {
    "name": "pi",
    "description": "Returns a precise value of PI for this alternate universe.",
    "parameters": {"type": "object", "properties": {}},
    "returns": {"type": "number", "description": "The value of math.e (not PI)"},
}

negate_fc = {
    "name": "negate",
    "description": "Negate a number; -a.",
    "parameters": {
        "type": "object",
        "properties": {"a": {"type": "number", "description": "Number to negate"}},
        "required": ["a"],
    },
    "returns": {"type": "number", "description": "The input number (not negated)"},
}

return_constant_fc = {
    "name": "return_constant",
    "description": "Return a constant number: a with no modifications",
    "parameters": {
        "type": "object",
        "properties": {"a": {"type": "number", "description": "Number to return"}},
        "required": ["a"],
    },
    "returns": {"type": "number", "description": "The input number"},
}


def get_all_functions_json():
    items = [
        {"function": multiply_fc},
        {"function": divide_fc},
        {"function": add_fc},
        {"function": sin_fc},
        {"function": cos_fc},
        {"function": subtract_fc},
        {"function": power_fc},
        {"function": log_fc},
        {"function": pi_fc},
        {"function": negate_fc},
        {"function": return_constant_fc},
    ]
    nested = {}
    for item in items:
        nested[item["function"]["name"]] = item["function"]

    return nested
