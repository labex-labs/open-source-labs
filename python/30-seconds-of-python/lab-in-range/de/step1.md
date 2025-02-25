# Zahl im Bereich

Schreiben Sie eine Funktion `in_range(n, start, end = 0)`, die drei Parameter annimmt:

- `n`: Eine Zahl, um zu überprüfen, ob sie innerhalb des Bereichs liegt
- `start`: Der Anfang des Bereichs
- `end`: Das Ende des Bereichs (optional, Standardwert ist 0)

Die Funktion sollte `True` zurückgeben, wenn die gegebene Zahl `n` innerhalb des angegebenen Bereichs liegt, andernfalls `False`. Wenn der Parameter `end` nicht angegeben ist, wird der Bereich als von `0` bis `start` betrachtet.

```python
def in_range(n, start, end = 0):
  return start <= n <= end if end >= start else end <= n <= start
```

```python
in_range(3, 2, 5) # True
in_range(3, 4) # True
in_range(2, 3, 5) # False
in_range(3, 2) # False
```
