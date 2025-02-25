# Index des passenden Elements finden

Schreiben Sie eine Funktion `find_index(lst, fn)`, die eine Liste `lst` und eine Testfunktion `fn` als Argumente übernimmt. Die Funktion sollte den Index des ersten Elements in `lst` zurückgeben, für das `fn` `True` zurückgibt.

```python
def find_index(lst, fn):
  return next(i for i, x in enumerate(lst) if fn(x))
```

```python
find_index([1, 2, 3, 4], lambda n: n % 2 == 1) # 0
```
