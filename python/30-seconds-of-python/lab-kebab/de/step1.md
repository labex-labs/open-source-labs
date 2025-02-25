# Kebab-Case-String

Schreiben Sie eine Python-Funktion namens `to_kebab_case(s)`, die einen String `s` als Eingabe nimmt und die Kebab-Case-Version des Strings zurückgibt. Die Funktion sollte die folgenden Schritte ausführen:

1. Ersetzen Sie jedes `-` oder `_` durch ein Leerzeichen, indem Sie die reguläre Ausdrucksmuster `r"(_|-)+"` verwenden.
2. Finden Sie alle Wörter im String und konvertieren Sie sie mit `str.lower()` in Kleinbuchstaben.
3. Verbinden Sie alle Wörter mit `-` als Separator.

```python
from re import sub

def kebab(s):
  return '-'.join(
    sub(r"(\s|_|-)+"," ",
    sub(r"[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+",
    lambda mo: ' ' + mo.group(0).lower(), s)).split())
```

```python
kebab('camelCase') # 'camel-case'
kebab('some text') # 'some-text'
kebab('some-mixed_string With spaces_underscores-and-hyphens')
# 'some-mixed-string-with-spaces-underscores-and-hyphens'
kebab('AllThe-small Things') # 'all-the-small-things'
```
