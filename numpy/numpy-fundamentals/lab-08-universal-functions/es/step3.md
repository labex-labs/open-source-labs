# Determinación del tipo de salida

La salida de una ufunc no necesariamente es un ndarray si no todos los argumentos de entrada son ndarrays. El tipo de salida se puede determinar en función de los tipos de entrada y las reglas de casteo de tipos. Echemos un ejemplo.

```python
import numpy as np

# Crea un array
arr = np.arange(9).reshape(3, 3)

# Realiza la multiplicación y especifica el tipo de salida
result = np.multiply.reduce(arr, dtype=float)

# Imprime el resultado
print(result)
```

Salida:

```
array([ 0., 28., 80.])
```
