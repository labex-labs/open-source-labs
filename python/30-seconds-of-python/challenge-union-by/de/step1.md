# Liste-Vereinigung basierend auf Funktion

## Problemstellung

Schreiben Sie eine Funktion `union_by(a, b, fn)`, die zwei Listen `a` und `b` sowie eine Funktion `fn` als Parameter erhält. Die Funktion sollte eine Liste zurückgeben, die jedes Element enthält, das in irgendeiner der beiden Listen vorkommt, wobei die bereitgestellte Funktion auf jedes Element beider Listen angewendet wird.

Um dieses Problem zu lösen, können Sie die folgenden Schritte ausführen:

1. Erstellen Sie eine `Menge`, indem Sie `fn` auf jedes Element in `a` anwenden.
2. Verwenden Sie eine Listenkomprehension in Kombination mit `fn` auf `b`, um nur die Werte zu behalten, die nicht in der zuvor erstellten Menge `_a` enthalten sind.
3. Schließlich erstellen Sie eine `Menge` aus dem vorherigen Ergebnis und `a` und wandeln sie diese in eine `Liste` um.

Die Funktion sollte die folgenden Eingabeparameter haben:

- `a`: Eine Liste von Elementen
- `b`: Eine Liste von Elementen
- `fn`: Eine Funktion, die ein Element nimmt und einen Wert zurückgibt

Die Funktion sollte eine Liste von Elementen zurückgeben.

## Beispiel

Hier ist ein Beispiel dafür, was `union_by()` tun sollte:

```python
from math import floor

union_by([2.1], [1.2, 2.3], floor) # [2.1, 1.2]
```

In diesem Beispiel nimmt `union_by()` zwei Listen `[2.1]` und `[1.2, 2.3]` sowie eine Funktion `floor()` entgegen. Die Funktion wendet `floor()` auf jedes Element beider Listen an und erstellt dabei eine Menge `{2}`. Anschließend verwendet sie eine Listenkomprehension, um nur die Werte zu behalten, die nicht in der Menge enthalten sind, was `[1.2]` ist. Schließlich erstellt sie eine Menge aus dem vorherigen Ergebnis und `[2.1]`, was `{1.2, 2.1}` ist, und wandelt diese in eine Liste `[1.2, 2.1]` um.
