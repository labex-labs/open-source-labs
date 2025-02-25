# Den letzten passenden Index finden

## Problem

Schreiben Sie eine Funktion `find_last_index(lst, fn)`, die eine Liste `lst` und eine Funktion `fn` als Argumente nimmt. Die Funktion sollte den Index des letzten Elements in `lst` zurückgeben, für das `fn` `True` zurückgibt. Wenn kein Element die Bedingung erfüllt, sollte die Funktion `-1` zurückgeben.

## Beispiel

```python
find_last_index([1, 2, 3, 4], lambda n: n % 2 == 1) # 2
find_last_index([2, 4, 6, 8], lambda n: n % 2 == 1) # -1
```
