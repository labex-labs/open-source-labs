# Testen, ob einige Listelemente wahrheitswertig sind

Schreiben Sie eine Funktion `some(lst, fn)`, die eine Liste `lst` und eine Funktion `fn` als Argumente nimmt. Die Funktion sollte `True` zurückgeben, wenn die Funktion `fn` für mindestens ein Element in der Liste `lst` `True` zurückgibt. Wenn kein Element in der Liste die Bedingung erfüllt, sollte die Funktion `False` zurückgeben. Wenn keine Funktion angegeben wird, sollte die Funktion die Identitätsfunktion verwenden (die das Element selbst zurückgibt).

```python
def some(lst, fn = lambda x: x):
  return any(map(fn, lst))
```

```python
some([0, 1, 2, 0], lambda x: x >= 2 ) # True
some([0, 0, 1, 0]) # True
```
