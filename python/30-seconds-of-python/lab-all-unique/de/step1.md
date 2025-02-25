# Funktion zum Überprüfen auf Duplikate in einer Liste

Schreiben Sie eine Python-Funktion namens `has_duplicates(lst)`, die eine Liste als Argument nimmt und `True` zurückgibt, wenn die Liste doppelte Elemente enthält, andernfalls `False`.

Um dieses Problem zu lösen, können Sie die folgenden Schritte ausführen:

1. Konvertieren Sie die Liste in einen Satz, um Duplikate zu entfernen.
2. Vergleichen Sie die Länge des Satzes mit der Länge der ursprünglichen Liste.
3. Wenn die Längen gleich sind, hat die Liste keine Duplikate, andernfalls hat sie Duplikate.

```python
def all_unique(lst):
  return len(lst) == len(set(lst))
```

```python
x = [1, 2, 3, 4, 5, 6]
y = [1, 2, 2, 3, 4, 5]
all_unique(x) # True
all_unique(y) # False
```
