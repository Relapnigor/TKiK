from enum import Enum


class TokenCode(Enum):
    LICZBACBZ = "LiczbaCBZ"
    PLUS = "+"
    MINUS = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    LN = "("
    RN = ")"
    UNKNOWN_CHARACTER_ERR = "Unknown character"
    END = "End"
