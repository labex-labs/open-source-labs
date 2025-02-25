# Operaciones aritméticas básicas

Las ufuncs básicas operan sobre escalares, y el ejemplo más simple es el operador de suma. Veamos cómo podemos usar el operador de suma para sumar dos arrays elemento a elemento.

```python
import numpy as np

# Crea dos arrays
arr1 = np.array([0, 2, 3, 4])
arr2 = np.array([1, 1, -1, 2])

# Suma los arrays elemento a elemento
result = arr1 + arr2

# Imprime el resultado
print(result)
```

Salida:

```
array([1, 3, 2, 6])
```
