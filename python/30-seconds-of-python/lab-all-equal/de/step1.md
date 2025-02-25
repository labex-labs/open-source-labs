# Überprüfen, ob alle Listelemente identisch sind

Schreiben Sie eine Funktion `all_equal(lst)`, die eine Liste als Argument nimmt und `True` zurückgibt, wenn alle Elemente in der Liste identisch sind, und `False` andernfalls.

Um dieses Problem zu lösen, können Sie die folgenden Schritte verwenden:

1. Verwenden Sie `set()`, um doppelte Elemente in der Liste zu eliminieren.
2. Verwenden Sie `len()`, um zu überprüfen, ob die Länge des Sets `1` ist.
3. Wenn die Länge des Sets `1` ist, geben Sie `True` zurück. Andernfalls geben Sie `False` zurück.

```python
def all_equal(lst):
  return len(set(lst)) == 1
```

```python
all_equal([1, 2, 3, 4, 5, 6]) # False
all_equal([1, 1, 1, 1]) # True
```
