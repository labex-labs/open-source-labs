# Mínimo Múltiplo Comum

Escreva uma função `lcm(numbers)` que recebe uma lista de números como argumento e retorna o seu mínimo múltiplo comum. Sua função deve usar a seguinte fórmula para calcular o MMC de dois números `x` e `y`: `lcm(x, y) = x * y / gcd(x, y)`, onde `gcd(x, y)` é o máximo divisor comum (MDC) de `x` e `y`.

Para resolver este problema, você pode usar a função `functools.reduce()` para aplicar a fórmula `lcm()` a todos os números na lista. Você também pode usar a função `math.gcd()` para calcular o máximo divisor comum de dois números.

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
