# Operaciones de Indexación

Las operaciones de indexación en NumPy pueden crear vistas o copias, dependiendo del tipo de indexación.

- La indexación básica siempre crea vistas. Por ejemplo:

```python
import numpy as np

# Crea un array
x = np.arange(10)

# Crea una vista
y = x[1:3]

# Modifica la vista
y[0] = 10

# Imprime el array original
print(x)  # Salida: [0, 10, 2, 3, 4, 5, 6, 7, 8, 9]
```

En el ejemplo anterior, la vista `y` refleja los cambios realizados en el array original `x`.

- La indexación avanzada siempre crea copias. Por ejemplo:

```python
import numpy as np

# Crea un array
x = np.arange(9).reshape(3, 3)

# Crea una copia
y = x[[1, 2]]

# Modifica el array original
x[[1, 2]] = [[10, 11, 12], [13, 14, 15]]

# Imprime la copia
print(y)  # Salida: [[3, 4, 5], [6, 7, 8]]
```

En el ejemplo anterior, la copia `y` permanece sin cambios después de modificar el array original `x`.
