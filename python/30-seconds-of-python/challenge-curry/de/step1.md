# Curry-Funktion

## Problemstellung

Schreiben Sie eine Funktion `curry(fn, *args)`, die eine gegebene Funktion `fn` curryiert. Die Funktion sollte eine neue Funktion zurückgeben, die sich wie `fn` mit den angegebenen Argumenten `args` verhält, wobei die Argumente teilweise angewendet sind.

## Beispiel

```python
add = lambda x, y: x + y
add10 = curry(add, 10)
add10(20) # 30
```
