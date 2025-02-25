# Replicar, unir o mutar arrays existentes

Una vez que has creado arrays, puedes replicarlos, unirlos o mutarlos para crear nuevos arrays. Cuando asignas un array o sus elementos a una nueva variable, utiliza la función `np.copy` para crear un nuevo array en lugar de una vista en el array original. Aquí hay un ejemplo:

```python
import numpy as np

# Crea un array
a = np.array([1, 2, 3, 4])

# Crea una vista de los primeros dos elementos del array
b = a[:2]

# Modifica la vista
b += 1

# Imprime el array original y la vista modificada
print('a =', a, '; b =', b)
```

Para unir arrays, puedes utilizar funciones como `np.vstack`, `np.hstack` y `np.block`. Aquí hay un ejemplo de unir cuatro arrays de 2x2 en un array de 4x4 utilizando `np.block`:

```python
import numpy as np

A = np.ones((2, 2))
B = np.eye(2)
C = np.zeros((2, 2))
D = np.diag((-3, -4))

resultado = np.block([[A, B], [C, D]])
```
