# Liste-Vereinigung basierend auf Funktion

Schreiben Sie eine Funktion `union_by(a, b, fn)`, die zwei Listen `a` und `b` sowie eine Funktion `fn` annimmt. Die Funktion sollte eine Liste zurückgeben, die jedes Element enthält, das in einer der beiden Listen vorkommt, nachdem die bereitgestellte Funktion auf jedes Element beider Listen angewendet wurde.

Um dieses Problem zu lösen, können Sie die folgenden Schritte ausführen:

1. Erstellen Sie einen `set`, indem Sie `fn` auf jedes Element in `a` anwenden.
2. Verwenden Sie eine Listenkomprehension in Kombination mit `fn` auf `b`, um nur die Werte zu behalten, die nicht in dem zuvor erstellten `set`, `_a`, enthalten sind.
3. Schließlich erstellen Sie aus dem vorherigen Ergebnis und `a` ein `set` und wandeln es in eine `Liste` um.

Die Funktion sollte die folgenden Eingabeparameter haben:

- `a`: Eine Liste von Elementen
- `b`: Eine Liste von Elementen
- `fn`: Eine Funktion, die ein Element annimmt und einen Wert zurückgibt

Die Funktion sollte eine Liste von Elementen zurückgeben.

```python
def union_by(a, b, fn):
  _a = set(map(fn, a))
  return list(set(a + [item for item in b if fn(item) not in _a]))
```

```python
from math import floor

union_by([2.1], [1.2, 2.3], floor) # [2.1, 1.2]
```
