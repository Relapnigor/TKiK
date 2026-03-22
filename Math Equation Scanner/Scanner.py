from Token import Token
from TokenCode import TokenCode


class Scanner:
    def __init__(self, source):
        self.source = source
        self.tokens = []

    def scan(self) -> list[Token]:
        pos = 0
        while pos < len(self.source):
            char = self.source[pos]
            if self.is_whitespace(char):
                pass
            elif self.is_digit(char):
                startpos = pos
                number, pos = self.get_number(char, pos)
                self.tokens.append(Token(TokenCode.LICZBACBZ, number, startpos))
            elif char in [code.value for code in TokenCode]:
                self.tokens.append(Token(TokenCode(char), char, pos))
            else:
                self.tokens.append(Token(TokenCode.UNKNOWN_CHARACTER_ERR, char, pos))
            pos += 1
        self.tokens.append(Token(TokenCode.END, "End", pos))

        return self.tokens

    def is_digit(self, char) -> bool:
        return char in "0123456789"

    def is_whitespace(self, char) -> bool:
        return char in " \t\n"

    def get_number(self, char, pos) -> tuple[str, int]:
        number = char
        while pos + 1 < len(self.source) and self.is_digit(self.source[pos + 1]):
            pos += 1
            number += self.source[pos]
        return number, pos
