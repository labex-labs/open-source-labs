# Máximo Común Divisor

Escribe una función llamada `gcd(numbers)` que tome una lista de enteros como argumento y devuelva su máximo común divisor. Tu función debe utilizar `functools.reduce()` y `math.gcd()` sobre la lista dada.

```python
from functools import reduce
from math import gcd as _gcd

def gcd(numbers):
  return reduce(_gcd, numbers)
```

```python
gcd([8, 36, 28]) # 4
```
