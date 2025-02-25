# Testen, ob einige Listelemente wahrheitswertig sind

## Problemstellung

Schreiben Sie eine Funktion `some(lst, fn)`, die eine Liste `lst` und eine Funktion `fn` als Argumente nimmt. Die Funktion sollte `True` zurückgeben, wenn die Funktion `fn` für mindestens ein Element in der Liste `lst` `True` zurückgibt. Wenn kein Element in der Liste die Bedingung erfüllt, sollte die Funktion `False` zurückgeben. Wenn keine Funktion angegeben wird, sollte die Funktion die Identitätsfunktion verwenden (die das Element selbst zurückgibt).

## Beispiel

```python
some([0, 1, 2, 0], lambda x: x >= 2 ) # True
some([0, 0, 1, 0]) # True
some(['', 'hello', 'world'], bool) # True
some(['', '', ''], bool) # False
```
