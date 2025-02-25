# Ejemplos de difusión (broadcasting)

Veamos algunos ejemplos para entender cómo funciona la difusión (broadcasting) en diferentes escenarios.

- Ejemplo 1:

```python
import numpy as np

a = np.array([[1.0, 2.0, 3.0],
              [4.0, 5.0, 6.0]])
b = np.array([1.0, 2.0, 3.0])
result = a + b
```

En este caso, `b` se suma a cada fila de `a`. El resultado es una matriz bidimensional con la misma forma que `a`, donde cada elemento es la suma de los elementos correspondientes en `a` y `b`.

- Ejemplo 2:

```python
import numpy as np

a = np.array([[1.0, 2.0, 3.0],
              [4.0, 5.0, 6.0]])
b = np.array([1.0, 2.0])
result = a + b
```

En este caso, la difusión (broadcasting) falla porque las dimensiones finales de `a` y `b` no son iguales. Es imposible alinear los valores en las filas de `a` con los elementos de `b` para la adición elemento a elemento.
