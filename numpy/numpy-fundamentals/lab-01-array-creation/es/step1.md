# Convertir secuencias de Python en arrays de NumPy

Para crear arrays de NumPy, puedes convertir secuencias de Python como listas y tuplas. Aquí te muestra cómo hacerlo:

```python
import numpy as np

# Crea un array 1D a partir de una lista
a1D = np.array([1, 2, 3, 4])

# Crea un array 2D a partir de una lista de listas
a2D = np.array([[1, 2], [3, 4]])

# Crea un array 3D a partir de listas anidadas
a3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
```

Al crear arrays, también puedes especificar el tipo de datos utilizando el parámetro `dtype`. Tien cuidado con las asignaciones de tipo de datos para evitar desbordamientos o resultados inesperados.
