# Liste Schnittmenge basierend auf Funktion

Schreiben Sie eine Funktion `intersection_by(a, b, fn)`, die zwei Listen `a` und `b` sowie eine Funktion `fn` annimmt. Die Funktion sollte eine Liste von Elementen zurückgeben, die in beiden Listen existieren, nachdem die bereitgestellte Funktion auf jedes Listenelement beider Listen angewendet wurde.

### Eingabe

- Zwei Listen `a` und `b` (1 <= len(a), len(b) <= 1000)
- Eine Funktion `fn`, die ein Argument annimmt und einen Wert zurückgibt

### Ausgabe

- Eine Liste von Elementen, die in beiden Listen existieren, nachdem die bereitgestellte Funktion auf jedes Listenelement beider Listen angewendet wurde.

```python
def intersection_by(a, b, fn):
  _b = set(map(fn, b))
  return [item for item in a if fn(item) in _b]
```

```python
from math import floor

intersection_by([2.1, 1.2], [2.3, 3.4], floor) # [2.1]
```
