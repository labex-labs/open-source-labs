# Überprüfen, ob eine Liste alle Werte enthält

Schreiben Sie eine Funktion namens `includes_all(lst, values)`, die zwei Listen als Parameter annimmt. Die Funktion sollte überprüfen, ob alle Werte in der `values`-Liste in der `lst`-Liste enthalten sind. Wenn alle Werte enthalten sind, sollte die Funktion `True` zurückgeben. Wenn irgendeiner der Werte nicht enthalten ist, sollte die Funktion `False` zurückgeben.

Um dieses Problem zu lösen, sollten Sie:

1. Einen `for`-Schleife verwenden, um durch jeden Wert in der `values`-Liste zu iterieren.
2. Überprüfen, ob der aktuelle Wert in der `lst`-Liste enthalten ist, indem Sie den `in`-Operator verwenden.
3. Wenn der Wert nicht enthalten ist, geben Sie `False` zurück.
4. Wenn alle Werte enthalten sind, geben Sie `True` zurück.

```python
def includes_all(lst, values):
  for v in values:
    if v not in lst:
      return False
  return True
```

```python
includes_all([1, 2, 3, 4], [1, 4]) # True
includes_all([1, 2, 3, 4], [1, 5]) # False
```
