# Convertendo sequências Python em Arrays NumPy

Para criar arrays NumPy, você pode converter sequências Python, como listas e tuplas. Veja como você pode fazer isso:

```python
import numpy as np

# Create a 1D array from a list
a1D = np.array([1, 2, 3, 4])

# Create a 2D array from a list of lists
a2D = np.array([[1, 2], [3, 4]])

# Create a 3D array from nested lists
a3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
```

Ao criar arrays, você também pode especificar o tipo de dado (data type) usando o parâmetro `dtype`. Tenha cuidado com as atribuições de tipo de dado para evitar overflow (estouro) ou resultados inesperados.
