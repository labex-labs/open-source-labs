# Eindeutige Liste-Werte filtern

Schreiben Sie eine Python-Funktion namens `filter_unique(lst)`, die eine Liste als Argument nimmt und eine neue Liste zurückgibt, die nur die nicht-eindeutigen Werte enthält. Um dieses Problem zu lösen, können Sie die folgenden Schritte ausführen:

1. Verwenden Sie `collections.Counter`, um die Anzahl jedes Werts in der Liste zu erhalten.
2. Verwenden Sie eine Listenkomprehension, um eine Liste zu erstellen, die nur die nicht-eindeutigen Werte enthält.

Ihre Funktion sollte die folgenden Anforderungen erfüllen:

- Die Funktion sollte eine Liste als Argument nehmen.
- Die Funktion sollte eine neue Liste zurückgeben, die nur die nicht-eindeutigen Werte enthält.
- Die Funktion sollte die ursprüngliche Liste nicht verändern.
- Die Funktion sollte case-sensitiv sein, was bedeutet, dass 'a' und 'A' als unterschiedliche Werte betrachtet werden.

```python
def filter_unique(lst):
    # Ihr Code hier
```

```python
from collections import Counter

def filter_unique(lst):
  return [item for item, count in Counter(lst).items() if count > 1]
```

```python
filter_unique([1, 2, 2, 3, 4, 4, 5]) # [2, 4]
```
