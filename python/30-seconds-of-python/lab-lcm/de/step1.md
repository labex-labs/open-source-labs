# Kleinste gemeinsame Vielfache

Schreiben Sie eine Funktion `lcm(numbers)`, die eine Liste von Zahlen als Argument nimmt und ihr kleinstes gemeinsames Vielfaches zurückgibt. Ihre Funktion sollte die folgende Formel verwenden, um das kgV von zwei Zahlen `x` und `y` zu berechnen: `kgV(x, y) = x * y / ggT(x, y)`, wobei `ggT(x, y)` der größte gemeinsame Teiler von `x` und `y` ist.

Um dieses Problem zu lösen, können Sie die Funktion `functools.reduce()` verwenden, um die `kgV()`-Formel auf alle Zahlen in der Liste anzuwenden. Sie können auch die Funktion `math.gcd()` verwenden, um den größten gemeinsamen Teiler von zwei Zahlen zu berechnen.

```python
from functools import reduce
from math import gcd

def lcm(numbers):
  return reduce((lambda x, y: int(x * y / gcd(x, y))), numbers)
```

```python
lcm([12, 7]) # 84
lcm([1, 3, 4, 5]) # 60
```
