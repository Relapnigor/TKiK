### Python 3.14.3

Skaner pobiera kod z pliku code.txt. Na jego podstawie generuje plik output.html z odpowiednim kolorowaniem składni.

### Rozpoznawane tokeny

| Kod       | Opis                                         | Kolor |
|-----------|---------------------------------------------|-------|
| KEYWORD   | if, else, while, for, return, func, true, false, null | #C792EA |
| VARIABLE  | Zmienne                                     | #53FCE5 |
| FUNC      | Nazwy funkcji                               | #F5F100 |
| TYPE      | int, float, string, bool, void             | #FFCB6B |
| STRING    | Tekst w cudzysłowie                         | #C3E88D |
| NUMBER    | Liczby                                      | #F78C6C |
| OPERATOR  | +, -, *, /, =, !, <, >                      | #546E7A |
| PAREN     | (, ), {, }, [, ]                             | #FF00FF |
| COMMENT   | Komentarze po #                              | #0DA000 |
| SPACE     | Spacje                                      | -  |
| NEWLINE   | Nowe linie                                  | -  |