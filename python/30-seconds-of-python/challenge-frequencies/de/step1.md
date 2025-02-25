# Wertfrequenzen

## Problem

Schreiben Sie eine Python-Funktion namens `value_frequencies(lst)`, die eine Liste als Argument nimmt und ein Dictionary zurückgibt, wobei die einzigartigen Werte der Liste als Schlüssel und ihre Häufigkeiten als Werte verwendet werden.

Um dieses Problem zu lösen, können Sie die folgenden Schritte ausführen:

1. Erstellen Sie ein leeres Dictionary, um die Häufigkeiten jedes einzelnen einzigartigen Elements zu speichern.
2. Iterieren Sie über die Liste und verwenden Sie `collections.defaultdict`, um die Häufigkeiten jedes einzelnen einzigartigen Elements zu speichern.
3. Verwenden Sie `dict()`, um ein Dictionary zurückzugeben, das die einzigartigen Elemente der Liste als Schlüssel und ihre Häufigkeiten als Werte hat.

Ihre Funktion sollte das Dictionary mit den einzigartigen Werten und ihren Häufigkeiten zurückgeben.

## Beispiel

```python
value_frequencies(['a', 'b', 'a', 'c', 'a', 'a', 'b']) # { 'a': 4, 'b': 2, 'c': 1 }
```
