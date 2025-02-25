# Número es primo

Escribe una función de Python llamada `is_prime(n)` que tome un entero `n` como entrada y devuelva `True` si el número es primo y `False` en caso contrario. Para resolver este problema, debes seguir estas reglas:

- Devuelve `False` si el número es `0`, `1`, un número negativo o un múltiplo de `2`.
- Utiliza `all()` y `range()` para comprobar los números desde `3` hasta la raíz cuadrada del número dado.
- Devuelve `True` si ninguno de ellos divide al número dado, `False` en caso contrario.

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
