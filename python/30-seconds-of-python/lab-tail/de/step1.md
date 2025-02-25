# Liste-Ende

Schreiben Sie eine Funktion `tail(lst)`, die eine Liste als Argument nimmt und alle Elemente in der Liste außer dem ersten zurückgibt. Wenn die Liste nur ein Element enthält, geben Sie die gesamte Liste zurück.

```python
def tail(lst):
  return lst[1:] if len(lst) > 1 else lst
```

```python
tail([1, 2, 3]) # [2, 3]
tail([1]) # [1]
```
