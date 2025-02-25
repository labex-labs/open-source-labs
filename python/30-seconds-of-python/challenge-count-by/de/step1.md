# Zählen gruppierter Elemente

## Problem

Schreiben Sie eine Funktion `count_by(lst, fn = lambda x: x)`, die eine Liste `lst` und eine Funktion `fn` als Argumente nimmt. Die Funktion sollte die Elemente der Liste basierend auf der angegebenen Funktion gruppieren und ein Dictionary zurückgeben, das die Anzahl der Elemente in jeder Gruppe enthält.

Um dieses Problem zu lösen, können Sie die folgenden Schritte ausführen:

1. Initialisieren Sie ein Dictionary mit `collections.defaultdict`.
2. Verwenden Sie `map()`, um die angegebene Funktion auf jedes Element der Liste anzuwenden.
3. Iterieren Sie über die gemappten Werte und erhöhen Sie die Anzahl jedes Elements im Dictionary.

Die Funktion sollte das resultierende Dictionary zurückgeben.

## Beispiel

```python
count_by([6.1, 4.2, 6.3], floor) # {6: 2, 4: 1}
count_by(['one', 'two', 'three'], len) # {3: 2, 5: 1}
```

Im ersten Beispiel wird die Funktion `floor` verwendet, um die Elemente der Liste `[6.1, 4.2, 6.3]` zu gruppieren. Das resultierende Dictionary hat zwei Schlüssel: `6` und `4`, mit den Werten `2` und `1` respectively.

Im zweiten Beispiel wird die Funktion `len` verwendet, um die Elemente der Liste `['one', 'two', 'three']` zu gruppieren. Das resultierende Dictionary hat zwei Schlüssel: `3` und `5`, mit den Werten `2` und `1` respectively.
