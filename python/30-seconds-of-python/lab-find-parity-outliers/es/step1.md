# Encuentra los valores atípicos de paridad

Escribe una función `find_parity_outliers(nums)` que tome una lista de enteros `nums` como argumento y devuelva una lista de todos los valores atípicos de paridad en `nums`.

Para resolver este problema, puedes seguir estos pasos:

1. Utiliza `collections.Counter` con una comprensión de listas para contar los valores pares e impares en la lista.
2. Utiliza `collections.Counter.most_common()` para obtener la paridad más común.
3. Utiliza una comprensión de listas para encontrar todos los elementos que no coinciden con la paridad más común.

```python
from collections import Counter

def find_parity_outliers(nums):
  return [
    x for x in nums
    if x % 2!= Counter([n % 2 for n in nums]).most_common()[0][0]
  ]
```

```python
find_parity_outliers([1, 2, 3, 4, 6]) # [1, 3]
```
