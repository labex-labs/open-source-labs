# Máximo Divisor Comum (Greatest Common Divisor)

Escreva uma função chamada `gcd(numbers)` que recebe uma lista de inteiros como argumento e retorna o seu máximo divisor comum. Sua função deve usar `functools.reduce()` e `math.gcd()` sobre a lista fornecida.

```python
from functools import reduce
from math import gcd as _gcd

def gcd(numbers):
  return reduce(_gcd, numbers)
```

```python
gcd([8, 36, 28]) # 4
```
