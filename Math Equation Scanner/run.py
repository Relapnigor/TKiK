import Scanner


def main():
    source = "2+3*(76+8/3)+ 3*(9-3)"
    scanner = Scanner.Scanner(str(source))
    tokens = scanner.scan()
    print(f"{'Position':<10}{'Code':<25}{'Value':<20}")
    print("-" * 50)
    for token in tokens:
        print(token)


if __name__ == "__main__":
    main()
