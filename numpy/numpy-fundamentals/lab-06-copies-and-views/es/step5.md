# Otras Operaciones

Hay otras operaciones en NumPy que pueden crear vistas o copias.

- La función `reshape()` crea una vista siempre que sea posible o una copia en caso contrario. Por ejemplo:

```python
import numpy as np

# Crea un array
x = np.ones((2, 3))

# Transpone el array
y = x.T

# Intenta cambiar la forma del array
try:
    y.shape = 6
except AttributeError:
    print("Incompatible shape for in-place modification. Use `.reshape()` to make a copy with the desired shape.")
```

En el ejemplo anterior, el array `y` se vuelve no contiguo después de la transposición, por lo que cambiar su forma requiere una copia.

- La función `ravel()` devuelve una vista aplanada contigua del array siempre que sea posible. Por otro lado, el método `flatten()` siempre devuelve una copia aplanada del array. Por ejemplo:

```python
import numpy as np

# Crea un array
x = np.arange(9).reshape(3, 3)

# Crea una vista aplanada
y = x.ravel()

# Crea una copia aplanada
z = x.flatten()

# Imprime el array original
print(x)  # Salida: [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
```

En el ejemplo anterior, `y` es una vista, mientras que `z` es una copia.
