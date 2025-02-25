# Die Liste vollständig entschachteln

Schreiben Sie eine Funktion `deep_flatten(lst)`, die eine Liste `lst` als Argument nimmt und eine neue Liste zurückgibt, die die vollständig entschachtelte Version von `lst` ist. Die Funktion sollte Rekursion verwenden und die `isinstance()`-Funktion mit `collections.abc.Iterable` verwenden, um zu überprüfen, ob ein Element iterierbar ist. Wenn ein Element iterierbar ist, sollte die Funktion `deep_flatten()` rekursiv auf das Element anwenden. Andernfalls sollte die Funktion eine Liste zurückgeben, die nur dieses Element enthält.

```python
from collections.abc import Iterable

def deep_flatten(lst):
  return ([a for i in lst for a in
          deep_flatten(i)] if isinstance(lst, Iterable) else [lst])
```

```python
deep_flatten([1, [2], [[3], 4], 5]) # [1, 2, 3, 4, 5]
```
