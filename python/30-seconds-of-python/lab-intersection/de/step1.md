# Schnittmenge von Listen

Schreibe eine Funktion `list_intersection(a, b)`, die zwei Listen `a` und `b` als Eingabe nimmt und eine neue Liste zurückgibt, die nur die Elemente enthält, die in beiden `a` und `b` vorhanden sind. Wenn es keine gemeinsamen Elemente gibt, sollte die Funktion eine leere Liste zurückgeben.

```python
def intersection(a, b):
  _a, _b = set(a), set(b)
  return list(_a & _b)
```

```python
intersection([1, 2, 3], [4, 3, 2]) # [2, 3]
```
