# Passendes Element finden

Schreiben Sie eine Funktion namens `find(lst, fn)`, die eine Liste `lst` und eine Testfunktion `fn` als Argumente übernimmt. Die Funktion sollte den Wert des ersten Elements in `lst` zurückgeben, für das `fn` `True` zurückgibt. Wenn kein Element der Testfunktion entspricht, sollte die Funktion `None` zurückgeben.

```python
def find(lst, fn):
  return next(x for x in lst if fn(x))
```

```python
find([1, 2, 3, 4], lambda n: n % 2 == 1) # 1
```
