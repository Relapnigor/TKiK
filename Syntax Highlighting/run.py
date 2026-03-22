from Scanner import Scanner
from pathlib import Path
from TokenColors import TokenColor


def run():
    path = Path(__file__).parent
    with open(path / "code.txt", "r") as file:
        code = file.read()

    scanner = Scanner(code)
    scanner.scan()

    html_output = (
        '<html><body style="background-color: #252525; font-size: 20px;"><pre>'
    )

    for token in scanner.tokens:
        if token.color not in [TokenColor.SPACE, TokenColor.NEWLINE]:
            html_output += (
                f'<span style="color: {token.color.value};">{token.value}</span>'
            )
        else:
            html_output += token.value

    html_output += "</pre></body></html>"

    with open(path / "output.html", "w") as file:
        file.write(html_output)


if __name__ == "__main__":
    run()
