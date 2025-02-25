# Creando Copias

Las copias se pueden crear duplicando tanto el búfer de datos como los metadatos de un array. Para crear una copia, puede utilizar el método `copy()` del objeto `ndarray`.

```python
import numpy as np

# Crea un array
x = np.array([1, 2, 3, 4, 5])

# Crea una copia
y = x.copy()

# Modifica la copia
y[0] = 10

# Imprime el array original
print(x)  # Salida: [1, 2, 3, 4, 5]
```

En el ejemplo anterior, la copia `y` es independiente del array original `x`.
