from TokenCode import TokenCode


class Token:
    def __init__(self, code: TokenCode, value: str, position: int):
        self.code = code
        self.value = value
        self.position = position

    def __str__(self):
        return f"{self.position:<10}{self.code.name:<25}{self.value:<20}"
