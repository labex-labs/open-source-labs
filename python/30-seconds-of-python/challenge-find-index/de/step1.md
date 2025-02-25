# Passendes Index finden

## Problem

Schreiben Sie eine Funktion `find_index(lst, fn)`, die eine Liste `lst` und eine Testfunktion `fn` als Argumente nimmt. Die Funktion sollte den Index des ersten Elements in `lst` zurückgeben, für das `fn` `True` zurückgibt.

## Beispiel

```python
find_index([1, 2, 3, 4], lambda n: n % 2 == 1) # 0
```
