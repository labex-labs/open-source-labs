# Ejemplo práctico - Cuantización vectorial

Exploremos un ejemplo práctico donde la difusión (broadcasting) es útil. Considere el algoritmo de cuantización vectorial (VQ) utilizado en teoría de la información y clasificación. La operación básica en VQ es encontrar el punto más cercano en un conjunto de puntos a un punto dado. Esto se puede hacer utilizando la difusión (broadcasting). Aquí hay un ejemplo:

```python
import numpy as np

observation = np.array([111.0, 188.0])
codes = np.array([[102.0, 203.0],
                  [132.0, 193.0],
                  [45.0, 155.0],
                  [57.0, 173.0]])
diff = codes - observation
dist = np.sqrt(np.sum(diff**2, axis=-1))
closest_index = np.argmin(dist)
closest_code = codes[closest_index]
```

En este ejemplo, `observation` representa el peso y la altura de un atleta a clasificar, y `codes` representa diferentes clases de atletas. Al restar `observation` de `codes`, se utiliza la difusión (broadcasting) para calcular la distancia entre `observation` y cada uno de los códigos. Luego, la función `argmin` se utiliza para encontrar el índice del código más cercano.
