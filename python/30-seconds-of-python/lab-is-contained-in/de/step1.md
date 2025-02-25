# Liste enthalten

Schreiben Sie eine Funktion `is_contained_in(a, b)`, die zwei Listen als Argumente nimmt und `True` zurückgibt, wenn alle Elemente der Liste `a` in der Liste `b` enthalten sind, unabhängig von der Reihenfolge. Andernfalls sollte die Funktion `False` zurückgeben.

Um dieses Problem zu lösen, können Sie den folgenden Ansatz verwenden:

1. Iterieren Sie über jedes einzigartige Element in der Liste `a`.
2. Für jedes Element überprüfen Sie, ob es in der Liste `a` öfter vorkommt als in der Liste `b`.
3. Wenn ein Element in der Liste `a` öfter vorkommt als in der Liste `b`, geben Sie `False` zurück.
4. Wenn alle Elemente in der Liste `a` in der Liste `b` mindestens so oft vorkommen wie in der Liste `a`, geben Sie `True` zurück.

```python
def is_contained_in(a, b):
  for v in set(a):
    if a.count(v) > b.count(v):
      return False
  return True
```

```python
is_contained_in([1, 4], [2, 4, 1]) # True
```
