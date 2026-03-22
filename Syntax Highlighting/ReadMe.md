### Python 3.14.3

Skaner pobiera kod z pliku code.txt. Na jego podstawie generuje plik output.html z odpowiednim kolorowaniem składni.

### Rozpoznawane tokeny

| Kod       | Opis                                         | Kolor       |
|-----------|---------------------------------------------|------------|
| KEYWORD   | if, else, while, for, return, func, true, false, null | <span style="display:inline-block;width:16px;height:16px;background-color:#C792EA;"></span> |
| VARIABLE  | Zmienne                                     | <span style="display:inline-block;width:16px;height:16px;background-color:#53FCE5;"></span> |
| FUNC      | Nazwy funkcji                               | <span style="display:inline-block;width:16px;height:16px;background-color:#F5F100;"></span> |
| TYPE      | int, float, string, bool, void             | <span style="display:inline-block;width:16px;height:16px;background-color:#FFCB6B;"></span> |
| STRING    | Tekst w cudzysłowie                         | <span style="display:inline-block;width:16px;height:16px;background-color:#C3E88D;"></span> |
| NUMBER    | Liczby                                      | <span style="display:inline-block;width:16px;height:16px;background-color:#F78C6C;"></span> |
| OPERATOR  | +, -, *, /, =, !, <, >                      | <span style="display:inline-block;width:16px;height:16px;background-color:#546E7A;"></span> |
| PAREN     | (, ), {, }, [, ]                             | <span style="display:inline-block;width:16px;height:16px;background-color:#FF00FF;"></span> |
| COMMENT   | Komentarze po #                              | <span style="display:inline-block;width:16px;height:16px;background-color:#0DA000;"></span> |
| SPACE     | Spacje                                      | -       |
| NEWLINE   | Nowe linie                                  | -       |