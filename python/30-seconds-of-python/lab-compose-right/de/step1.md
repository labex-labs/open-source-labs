# Umgekehrte Kompositionsfunktionen

Schreiben Sie eine Funktion `compose_right`, die eine oder mehrere Funktionen als Argumente nimmt und eine neue Funktion zurückgibt, die eine links-rechts-Funktionskomposition durchführt. Die erste (am linkesten) Funktion kann ein oder mehrere Argumente akzeptieren; die verbleibenden Funktionen müssen einstellige sein.

Ihre Implementierung sollte die `reduce`-Funktion aus dem `functools`-Modul verwenden, um die links-rechts-Funktionskomposition durchzuführen.

```python
from functools import reduce

def compose_right(*fns):
  # Ihr Code hier
```

```python
from functools import reduce

def compose_right(*fns):
  return reduce(lambda f, g: lambda *args: g(f(*args)), fns)
```

```python
add = lambda x, y: x + y
square = lambda x: x * x
add_and_square = compose_right(add, square)
add_and_square(1, 2) # 9
```
