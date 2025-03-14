# Listenunterschied basierend auf einer Funktion

Erstellen Sie eine Funktion namens `difference_by(a, b, fn)`, die drei Parameter annimmt:

- `a`: Eine Liste von Elementen
- `b`: Eine Liste von Elementen
- `fn`: Eine Funktion, die auf jedes Element in beiden Listen angewendet wird

Die Funktion sollte eine Liste von Elementen zurückgeben, die in der Liste `a` vorhanden sind, aber nicht in der Liste `b`, nachdem die bereitgestellte Funktion `fn` auf jedes Element in beiden Listen angewendet wurde.

Um dieses Problem zu lösen, können Sie die folgenden Schritte ausführen:

1. Erstellen Sie einen `Set`, indem Sie `map()` verwenden, um `fn` auf jedes Element in `b` anzuwenden.
2. Verwenden Sie eine Listenkomprehension in Kombination mit `fn` auf `a`, um nur die Werte zu behalten, die nicht im zuvor erstellten Set, `_b`, enthalten sind.

```python
def difference_by(a, b, fn):
  _b = set(map(fn, b))
  return [item for item in a if fn(item) not in _b]
```

```python
from math import floor

difference_by([2.1, 1.2], [2.3, 3.4], floor) # [1.2]
difference_by([{ 'x': 2 }, { 'x': 1 }], [{ 'x': 1 }], lambda v : v['x'])
# [ { x: 2 } ]
```
