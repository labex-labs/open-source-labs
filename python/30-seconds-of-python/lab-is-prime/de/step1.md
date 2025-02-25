# Zahl ist Primzahl

Schreiben Sie eine Python-Funktion namens `is_prime(n)`, die eine ganze Zahl `n` als Eingabe nimmt und `True` zurückgibt, wenn die Zahl eine Primzahl ist, und `False` sonst. Um dieses Problem zu lösen, müssen Sie die folgenden Regeln befolgen:

- Geben Sie `False` zurück, wenn die Zahl `0`, `1`, eine negative Zahl oder ein Vielfaches von `2` ist.
- Verwenden Sie `all()` und `range()` zum Überprüfen von Zahlen von `3` bis zur Quadratwurzel der gegebenen Zahl.
- Geben Sie `True` zurück, wenn keine Zahl die gegebene Zahl teilt, `False` sonst.

```python
from math import sqrt

def is_prime(n):
  if n <= 1 or (n % 2 == 0 and n > 2):
    return False
  return all(n % i for i in range(3, int(sqrt(n)) + 1, 2))
```

```python
is_prime(11) # True
```
