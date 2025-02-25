# Kebab-Case-String

## Problem

Schreiben Sie eine Python-Funktion namens `to_kebab_case(s)`, die einen String `s` als Eingabe nimmt und die Kebab-Case-Version des Strings zurückgibt. Die Funktion sollte die folgenden Schritte ausführen:

1. Ersetzen Sie alle `-` oder `_` durch ein Leerzeichen, indem Sie die reguläre Ausdrucksmuster `r"(_|-)+"` verwenden.
2. Finden Sie alle Wörter im String und konvertieren Sie sie mit `str.lower()` in Kleinbuchstaben.
3. Verbinden Sie alle Wörter mit `-` als Separator.

## Beispiel

```python
to_kebab_case('camelCase') # 'camel-case'
to_kebab_case('some text') # 'some-text'
to_kebab_case('some-mixed_string With spaces_underscores-and-hyphens')
# 'some-mixed-string-with-spaces-underscores-and-hyphens'
to_kebab_case('AllThe-small Things') # 'all-the-small-things'
```
