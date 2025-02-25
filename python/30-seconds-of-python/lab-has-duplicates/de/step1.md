# Überprüfen auf Duplikate in einer Liste

Schreiben Sie eine Python-Funktion namens `has_duplicates(lst)`, die eine Liste als Argument nimmt und `True` zurückgibt, wenn die Liste Duplikate enthält, und `False` andernfalls.

Um dieses Problem zu lösen, können Sie die folgenden Schritte verwenden:

1. Verwenden Sie die `set()`-Funktion, um Duplikate aus der Liste zu entfernen.
2. Vergleichen Sie die Länge der ursprünglichen Liste mit der Länge des Sets. Wenn sie gleich sind, dann gibt es keine Duplikate. Wenn sie unterschiedlich sind, dann gibt es Duplikate.

```python
def has_duplicates(lst):
  return len(lst)!= len(set(lst))
```

```python
x = [1, 2, 3, 4, 5, 5]
y = [1, 2, 3, 4, 5]
has_duplicates(x) # True
has_duplicates(y) # False
```
