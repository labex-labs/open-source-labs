# Snakecase String

## Problem

Schreiben Sie eine Python-Funktion namens `snake`, die einen String als Argument nimmt und den String im snake case Format zurückgibt. Die Funktion sollte die folgenden Schritte ausführen:

1. Verwenden Sie `re.sub()`, um alle Wörter im String zu finden, und `str.lower()`, um sie in Kleinbuchstaben umzuwandeln.
2. Verwenden Sie `re.sub()`, um alle `-`-Zeichen durch Leerzeichen zu ersetzen.
3. Verwenden Sie schließlich `str.join()`, um alle Wörter mit `_` als Separator zu kombinieren.

Ihre Funktion sollte Strings mit einem Gemisch aus Groß- und Kleinbuchstaben, Leerzeichen, Bindestrichen und Unterstrichen verarbeiten können.

## Beispiel

```python
snake('camelCase') # 'camel_case'
snake('some text') # 'some_text'
snake('some-mixed_string With spaces_underscores-and-hyphens')
# 'some_mixed_string_with_spaces_underscores_and_hyphens'
snake('AllThe-small Things') # 'all_the_small_things'
```
