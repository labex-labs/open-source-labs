# Métodos de ufunc

Las ufuncs tienen cuatro métodos: reduce, accumulate, reduceat y outer. Estos métodos son útiles para realizar operaciones en arrays. Echemos un vistazo al método reduce.

```python
import numpy as np

# Crea un array
arr = np.arange(9).reshape(3, 3)

# Reduce el array a lo largo del primer eje
result = np.add.reduce(arr, 1)

# Imprime el resultado
print(result)
```

Salida:

```
array([ 3, 12, 21])
```
