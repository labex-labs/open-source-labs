# Passendes Element finden

## Problemstellung

Schreiben Sie eine Funktion namens `find(lst, fn)`, die eine Liste `lst` und eine Testfunktion `fn` als Argumente übernimmt. Die Funktion sollte den Wert des ersten Elements in `lst` zurückgeben, für das `fn` `True` zurückgibt. Wenn kein Element der Testfunktion entspricht, sollte die Funktion `None` zurückgeben.

## Beispiel

```python
find([1, 2, 3, 4], lambda n: n % 2 == 1) # 1
find(['apple', 'banana', 'cherry'], lambda s: s.startswith('b')) # 'banana'
find([2, 4, 6, 8], lambda n: n % 2 == 1) # None
```
