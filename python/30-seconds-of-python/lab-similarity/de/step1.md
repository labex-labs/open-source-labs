# Listenähnlichkeit

Schreiben Sie eine Funktion `ähnlichkeit(a, b)`, die zwei Listen `a` und `b` als Argumente nimmt und eine neue Liste zurückgibt, die nur die Elemente enthält, die in beiden `a` und `b` vorhanden sind.

Um dieses Problem zu lösen, können wir List Comprehension verwenden, um über die Elemente von `a` zu iterieren und zu überprüfen, ob sie in `b` vorhanden sind. Wenn ein Element in beiden Listen vorhanden ist, fügen wir es einer neuen Liste hinzu.

```python
def ähnlichkeit(a, b):
  return [item for item in a if item in b]
```

```python
ähnlichkeit([1, 2, 3], [1, 2, 4]) # [1, 2]
```
