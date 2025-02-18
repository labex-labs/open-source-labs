# Snake Case Zeichenkette

Schreiben Sie eine Python-Funktion namens `snake`, die eine Zeichenkette als Argument nimmt und die Zeichenkette im Snake Case zurückgibt. Die Funktion sollte die folgenden Schritte ausführen:

1. Verwenden Sie `re.sub()`, um alle Wörter in der Zeichenkette zu finden, und `str.lower()`, um sie in Kleinbuchstaben umzuwandeln.
2. Verwenden Sie `re.sub()`, um alle `-`-Zeichen durch Leerzeichen zu ersetzen.
3. Verwenden Sie schließlich `str.join()`, um alle Wörter mit `_` als Trennzeichen zu verbinden.

Ihre Funktion sollte in der Lage sein, Zeichenketten mit einer Mischung aus Groß- und Kleinbuchstaben, Leerzeichen, Bindestrichen und Unterstrichen zu verarbeiten.

```python
from re import sub

def snake(s):
  return '_'.join(
    sub('([A-Z][a-z]+)', r' \1',
    sub('([A-Z]+)', r' \1',
    s.replace('-', ' '))).split()).lower()
```

```python
snake('camelCase') # 'camel_case'
snake('some text') # 'some_text'
snake('some-mixed_string With spaces_underscores-and-hyphens')
# 'some_mixed_string_with_spaces_underscores_and_hyphens'
snake('AllThe-small Things') # 'all_the_small_things'
```
