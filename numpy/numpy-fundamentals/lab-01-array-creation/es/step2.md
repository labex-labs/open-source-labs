# Usar funciones de creación de arrays intrínsecas de NumPy

NumPy proporciona funciones integradas para crear arrays. Aquí hay algunos ejemplos:

```python
import numpy as np

# Crea un array 1D con valores que aumentan regularmente
arr1D = np.arange(10)

# Crea un array 1D con un tipo de datos específico
arr1D_float = np.arange(2, 10, dtype=float)

# Crea un array 1D con un número específico de elementos
arr1D_linspace = np.linspace(1., 4., 6)

# Crea una matriz identidad 2D
matriz_identidad = np.eye(3)

# Crea una matriz 2D con valores dados a lo largo de la diagonal
matriz_diag = np.diag([1, 2, 3])

# Crea una matriz de Vandermonde
matriz_vander = np.vander([1, 2, 3, 4], 2)

# Crea un array lleno de ceros
array_ceros = np.zeros((2, 3))

# Crea un array lleno de unos
array_unos = np.ones((2, 3))

# Crea un array lleno de valores aleatorios
array_aleatorio = np.random.default_rng(42).random((2, 3))
```
