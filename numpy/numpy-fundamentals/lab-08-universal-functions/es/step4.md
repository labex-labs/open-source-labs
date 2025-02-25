# Difusión (Broadcasting)

La difusión es una característica poderosa de las ufuncs que permite realizar operaciones en arrays con diferentes formas. Las reglas de difusión determinan cómo se tratan los arrays con diferentes formas durante las operaciones. Echemos un ejemplo.

```python
import numpy as np

# Crea dos arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([[1], [2], [3]])

# Multiplica los arrays
result = arr1 * arr2

# Imprime el resultado
print(result)
```

Salida:

```
array([[1, 2, 3],
       [2, 4, 6],
       [3, 6, 9]])
```
