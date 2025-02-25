# Wertfrequenzen

Schreiben Sie eine Python-Funktion namens `value_frequencies(lst)`, die eine Liste als Argument nimmt und ein Dictionary zurückgibt, wobei die eindeutigen Werte der Liste als Schlüssel und ihre Frequenzen als Werte verwendet werden.

Um dieses Problem zu lösen, können Sie die folgenden Schritte ausführen:

1. Erstellen Sie ein leeres Dictionary, um die Frequenzen jedes eindeutigen Elements zu speichern.
2. Iterieren Sie über die Liste und verwenden Sie `collections.defaultdict`, um die Frequenzen jedes eindeutigen Elements zu speichern.
3. Verwenden Sie `dict()`, um ein Dictionary zurückzugeben, das die eindeutigen Elemente der Liste als Schlüssel und ihre Frequenzen als Werte hat.

Ihre Funktion sollte das Dictionary mit den eindeutigen Werten und ihren Frequenzen zurückgeben.

```python
from collections import defaultdict

def frequencies(lst):
  freq = defaultdict(int)
  for val in lst:
    freq[val] += 1
  return dict(freq)
```

```python
frequencies(['a', 'b', 'a', 'c', 'a', 'a', 'b']) # { 'a': 4, 'b': 2, 'c': 1 }
```
