# Diffusion (broadcasting) avec des tableaux de même forme

Dans le cas le plus simple, deux tableaux doivent avoir exactement la même forme pour effectuer des opérations élément par élément. Par exemple :

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 2.0, 2.0])
result = a * b
```

Dans ce cas, `a` et `b` ont la même forme, donc la multiplication est effectuée élément par élément et le résultat est `[2.0, 4.0, 6.0]`.
