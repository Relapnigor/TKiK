from Token import Token
from TokenColors import TokenColor
from TokenWords import TokenWords


class Scanner:
    def __init__(self, code: str):
        self.code = code
        self.tokens = []

    def scan(self):
        words = self.get_words()
        for i, word in enumerate(words):
            if word in TokenWords.KEYWORDS.value:
                self.tokens.append(Token(word, TokenColor.KEYWORD))
            elif word in TokenWords.TYPES.value:
                self.tokens.append(Token(word, TokenColor.TYPE))
            elif word.startswith("#"):
                self.tokens.append(Token(word, TokenColor.COMMENT))
            elif word in TokenWords.PARENS.value:
                self.tokens.append(Token(word, TokenColor.PAREN))
            elif word in TokenWords.OPERATORS.value:
                self.tokens.append(Token(word, TokenColor.OPERATOR))
            elif word.startswith('"') and word.endswith('"'):
                self.tokens.append(Token(word, TokenColor.STRING))
            elif i + 1 < len(words) and words[i + 1] == "(":
                self.tokens.append(Token(word, TokenColor.FUNC))
            elif self.is_number(word):
                self.tokens.append(Token(word, TokenColor.NUMBER))
            elif word == "\n":
                self.tokens.append(Token(word, TokenColor.NEWLINE))
            elif word in " \t":
                self.tokens.append(Token(word, TokenColor.SPACE))
            else:
                self.tokens.append(Token(word, TokenColor.VARIABLE))

    def get_words(self) -> list:
        words = []
        word = ""
        i = 0
        n = len(self.code)

        separators = " \t\n(){}[]+-*/=!<>"

        while i < n:
            char = self.code[i]
            if char == "#":
                comment = char
                i += 1
                while i < n and self.code[i] != "\n":
                    comment += self.code[i]
                    i += 1
                words.append(comment)
            elif char == '"':
                str_word = char
                i += 1

                while i < n and self.code[i] != '"':
                    str_word += self.code[i]
                    i += 1

                if i < n:
                    str_word += self.code[i]
                    i += 1
                words.append(str_word)
            elif char not in separators:
                word += char
                i += 1
            else:
                if word:
                    words.append(word)
                    word = ""
                if char in separators:
                    words.append(char)
                i += 1

        if word:
            words.append(word)

        return words

    def is_number(self, word: str) -> bool:
        try:
            float(word)
            return True
        except ValueError:
            return False
