from enum import Enum


class TokenColor(Enum):
    KEYWORD = "#C792EA"
    VARIABLE = "#53FCE5"
    FUNC = "#F5F100"
    TYPE = "#FFCB6B"
    STRING = "#C3E88D"
    NUMBER = "#F78C6C"
    OPERATOR = "#546E7A"
    PAREN = "#FF00FF"
    COMMENT = "#0DA000"
    SPACE = "SPACE"
    NEWLINE = "NEWLINE"
