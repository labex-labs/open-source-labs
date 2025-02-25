# Listenähnlichkeit

## Problemstellung

Schreiben Sie eine Funktion `ähnlichkeit(a, b)`, die zwei Listen `a` und `b` als Argumente nimmt und eine neue Liste zurückgibt, die nur die Elemente enthält, die in beiden `a` und `b` vorhanden sind.

Um dieses Problem zu lösen, können wir List Comprehension verwenden, um über die Elemente von `a` zu iterieren und zu überprüfen, ob sie in `b` vorhanden sind. Wenn ein Element in beiden Listen vorhanden ist, fügen wir es einer neuen Liste hinzu.

## Beispiel

```python
ähnlichkeit([1, 2, 3], [1, 2, 4]) # [1, 2]
```

In diesem Beispiel nimmt die Funktion `ähnlichkeit` zwei Listen `[1, 2, 3]` und `[1, 2, 4]` als Argumente. Die Funktion gibt eine neue Liste `[1, 2]` zurück, die nur die Elemente enthält, die in beiden Listen vorhanden sind.
