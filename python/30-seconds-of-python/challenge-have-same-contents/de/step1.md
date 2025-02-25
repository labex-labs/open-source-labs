# Überprüfen, ob zwei Listen den gleichen Inhalt haben

## Problemstellung

Schreiben Sie eine Funktion `have_same_contents(a, b)`, die zwei Listen als Argumente nimmt und `True` zurückgibt, wenn sie den gleichen Inhalt haben, andernfalls `False`. Die Funktion sollte überprüfen, ob die beiden Listen die gleichen Elemente enthalten, unabhängig von ihrer Reihenfolge.

Um dieses Problem zu lösen, können Sie die folgenden Schritte ausführen:

1. Verwenden Sie `set()` auf der Kombination beider Listen, um die eindeutigen Werte zu finden.
2. Iterieren Sie über sie mit einer `for-Schleife` und vergleichen Sie die `count()` jedes eindeutigen Werts in jeder Liste.
3. Geben Sie `False` zurück, wenn die Zählungen für irgendein Element nicht übereinstimmen, andernfalls `True`.

## Beispiel

```python
have_same_contents([1, 2, 4], [2, 4, 1]) # True
have_same_contents([1, 2, 4], [2, 4, 5]) # False
```
