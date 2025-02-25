# Zählen gruppierter Elemente

Schreiben Sie eine Funktion `count_by(lst, fn = lambda x: x)`, die eine Liste `lst` und eine Funktion `fn` als Argumente nimmt. Die Funktion sollte die Elemente der Liste basierend auf der angegebenen Funktion gruppieren und ein Dictionary zurückgeben, das die Anzahl der Elemente in jeder Gruppe enthält.

Um dieses Problem zu lösen, können Sie die folgenden Schritte ausführen:

1. Initialisieren Sie ein Dictionary mit `collections.defaultdict`.
2. Verwenden Sie `map()`, um die angegebene Funktion auf jedes Element der Liste anzuwenden.
3. Iterieren Sie über die gemappten Werte und erhöhen Sie die Anzahl jedes Elements im Dictionary.

Die Funktion sollte das resultierende Dictionary zurückgeben.

```python
from collections import defaultdict

def count_by(lst, fn = lambda x: x):
  count = defaultdict(int)
  for val in map(fn, lst):
    count[val] += 1
  return dict(count)
```

```python
from math import floor

count_by([6.1, 4.2, 6.3], floor) # {6: 2, 4: 1}
count_by(['one', 'two', 'three'], len) # {3: 2, 5: 1}
```
