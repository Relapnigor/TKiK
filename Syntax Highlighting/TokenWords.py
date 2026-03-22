from enum import Enum


class TokenWords(Enum):
    KEYWORDS = {"if", "else", "while", "for", "return", "func", "true", "false", "null"}
    TYPES = {"int", "float", "string", "bool", "void"}
    PARENS = {"(", ")", "{", "}", "[", "]"}
    OPERATORS = {"+", "-", "*", "/", "=", "!", "<", ">"}
