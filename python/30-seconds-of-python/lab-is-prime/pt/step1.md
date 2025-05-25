# Número é Primo

Escreva uma função Python chamada `is_prime(n)` que recebe um inteiro `n` como entrada e retorna `True` se o número for primo e `False` caso contrário. Para resolver este problema, você precisa seguir estas regras:

- Retorne `False` se o número for `0`, `1`, um número negativo ou um múltiplo de `2`.
- Use `all()` e `range()` para verificar números de `3` até a raiz quadrada do número fornecido.
- Retorne `True` se nenhum número dividir o número fornecido, `False` caso contrário.

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
