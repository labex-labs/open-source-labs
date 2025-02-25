# Curry-Funktion

Schreiben Sie eine Funktion `curry(fn, *args)`, die eine gegebene Funktion `fn` curriert. Die Funktion sollte eine neue Funktion zurückgeben, die sich wie `fn` mit den angegebenen Argumenten `args` verhält, wobei die Argumente teilweise angewendet sind.

```python
from functools import partial

def curry(fn, *args):
  return partial(fn, *args)
```

```python
add = lambda x, y: x + y
add10 = curry(add, 10)
add10(20) # 30
```
