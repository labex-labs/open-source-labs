# Funktionen zusammensetzen

Schreiben Sie eine Funktion namens `compose(*fns)`, die eine oder mehrere Funktionen als Argumente akzeptiert und eine neue Funktion zurückgibt, die das Ergebnis der Komposition der Eingabefunktionen von rechts nach links ist. Die letzte (rechtsmöglichste) Funktion kann ein oder mehrere Argumente akzeptieren; die verbleibenden Funktionen müssen einstellige sein.

```python
from functools import reduce

def compose(*fns):
  return reduce(lambda f, g: lambda *args: f(g(*args)), fns)
```

```python
add5 = lambda x: x + 5
multiply = lambda x, y: x * y
multiply_and_add_5 = compose(add5, multiply)
multiply_and_add_5(5, 2) # 15
```
