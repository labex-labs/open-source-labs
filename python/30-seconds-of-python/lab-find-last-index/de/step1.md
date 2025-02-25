# Den letzten passenden Index finden

Schreiben Sie eine Funktion `find_last_index(lst, fn)`, die eine Liste `lst` und eine Funktion `fn` als Argumente nimmt. Die Funktion sollte den Index des letzten Elements in `lst` zurückgeben, für das `fn` `True` zurückgibt. Wenn kein Element die Bedingung erfüllt, sollte die Funktion `-1` zurückgeben.

```python
def find_last_index(lst, fn):
  return len(lst) - 1 - next(i for i, x in enumerate(lst[::-1]) if fn(x))
```

```python
find_last_index([1, 2, 3, 4], lambda n: n % 2 == 1) # 2
```
