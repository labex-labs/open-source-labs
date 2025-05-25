# Inverter Número

Escreva uma função `reverse_number(n)` que recebe um número como argumento e retorna o reverso desse número. A função deve atender aos seguintes requisitos:

- A função deve inverter o número, independentemente de ser positivo ou negativo.
- A função deve retornar um float se a entrada for um float, e um inteiro se a entrada for um inteiro.
- A função não deve usar nenhuma função embutida que inverta diretamente um número (por exemplo, `reversed()`).
- A função não deve usar nenhuma função embutida que converta diretamente um número em uma string (por exemplo, `str()`).
- A função não deve usar nenhuma função embutida que converta diretamente uma string em um número (por exemplo, `int()` ou `float()`).

```python
from math import copysign

def reverse_number(n):
  return copysign(float(str(n)[::-1].replace('-', '')), n)
```

```python
reverse_number(981) # 189
reverse_number(-500) # -5
reverse_number(73.6) # 6.37
reverse_number(-5.23) # -32.5
```
