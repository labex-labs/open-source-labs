# Symmetrische Differenz basierend auf einer Funktion

Schreiben Sie eine Funktion `symmetric_difference_by(a, b, fn)`, die zwei Listen `a` und `b` sowie eine Funktion `fn` annimmt. Die Funktion sollte eine neue Liste zurückgeben, die alle Elemente enthält, die in einer der ursprünglichen Listen vorhanden sind, aber nicht in beiden, nachdem die bereitgestellte Funktion auf jedes Listelement beider Listen angewendet wurde.

Um dieses Problem zu lösen, können Sie die folgenden Schritte ausführen:

1. Erstellen Sie eine `Menge`, indem Sie `fn` auf jedes Element in jeder Liste anwenden.
2. Verwenden Sie eine Listenkomprehension in Kombination mit `fn` auf jeder der beiden Listen, um nur die Werte zu behalten, die nicht in der zuvor erstellten Menge der anderen Liste enthalten sind.
3. Verketten Sie die beiden Listen, die in Schritt 2 erhalten wurden.

Die Funktion sollte die folgenden Parameter haben:

- `a`: Eine Liste von Elementen
- `b`: Eine Liste von Elementen
- `fn`: Eine Funktion, die ein Element annimmt und einen neuen Wert zurückgibt

Die Funktion sollte eine neue Liste zurückgeben, die alle Elemente enthält, die in einer der ursprünglichen Listen vorhanden sind, aber nicht in beiden, nachdem die bereitgestellte Funktion auf jedes Listelement beider Listen angewendet wurde.

```python
def symmetric_difference_by(a, b, fn):
  (_a, _b) = (set(map(fn, a)), set(map(fn, b)))
  return [item for item in a if fn(item) not in _b] + [item
          for item in b if fn(item) not in _a]
```

```python
from math import floor

symmetric_difference_by([2.1, 1.2], [2.3, 3.4], floor) # [1.2, 3.4]
```
