# String zu Wörtern Herausforderung

## Problem

Schreiben Sie eine Funktion `string_to_words(s: str, pattern: str = '[a-zA-Z-]+') -> List[str]`, die einen String `s` und einen optionalen `pattern`-String als Argumente nimmt und eine Liste der Wörter im String zurückgibt.

- Die Funktion sollte `re.findall()` mit dem angegebenen `pattern` verwenden, um alle passenden Teilstrings zu finden.
- Wenn das `pattern`-Argument nicht angegeben wird, sollte die Funktion die Standard-Regulärausdruck verwenden, der alphanumerische Zeichen und Bindestriche übereinstimmt.

## Beispiel

```python
string_to_words('I love Python!!') # ['I', 'love', 'Python']
string_to_words('python, javaScript & coffee') # ['python', 'javaScript', 'coffee']
string_to_words('build -q --out one-item', r'\b[a-zA-Z-]+\b') # ['build', 'q', 'out', 'one-item']
```
