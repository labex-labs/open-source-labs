# Creando Vistas

Las vistas se pueden crear cambiando ciertos metadatos de un array. Esto crea una nueva forma de ver los datos sin copiarlos. Para crear una vista, puede utilizar el método `view()` del objeto `ndarray`.

```python
import numpy as np

# Crea un array
x = np.array([1, 2, 3, 4, 5])

# Crea una vista
y = x.view()

# Modifica la vista
y[0] = 10

# Imprime el array original
print(x)  # Salida: [10, 2, 3, 4, 5]
```

En el ejemplo anterior, la vista `y` nos permite modificar el array original `x`.
