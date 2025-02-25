# Größter gemeinsamer Teiler

Schreiben Sie eine Funktion namens `gcd(numbers)`, die eine Liste von ganzen Zahlen als Argument nimmt und deren größten gemeinsamen Teiler zurückgibt. Ihre Funktion sollte `functools.reduce()` und `math.gcd()` über die gegebene Liste verwenden.

```python
from functools import reduce
from math import gcd as _gcd

def gcd(numbers):
  return reduce(_gcd, numbers)
```

```python
gcd([8, 36, 28]) # 4
```
