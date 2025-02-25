# Determinando si un Array es una Vista o una Copia

Puede utilizar el atributo `base` del objeto `ndarray` para determinar si un array es una vista o una copia. El atributo `base` devuelve el array original para una vista y `None` para una copia. Por ejemplo:

```python
import numpy as np

# Crea un array
x = np.arange(9)

# Crea una vista
y = x.reshape(3, 3)

# Crea una copia
z = y[[2, 1]]

# Verifica si y es una vista
print(y.base)  # Salida: [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Verifica si z es una copia
print(z.base is None)  # Salida: True
```

En el ejemplo anterior, `y` es una vista y `z` es una copia.
