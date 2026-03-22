from TokenColors import TokenColor


class Token:
    def __init__(self, value: str, color: TokenColor):
        self.value = value
        self.color = color

    def __str__(self):
        return f"{self.color.name:<25}{self.value:<25}{self.color.value:<25}"
