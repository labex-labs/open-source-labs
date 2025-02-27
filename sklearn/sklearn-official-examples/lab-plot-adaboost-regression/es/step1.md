# Preparando los datos

Comenzamos preparando datos ficticios con una relación sinusoidal y algo de ruido gaussiano. Usamos la función `linspace()` de Numpy para crear una matriz unidimensional de 100 valores espaciados uniformemente entre 0 y 6. Luego usamos el atributo `np.newaxis` para convertir la matriz unidimensional en una matriz bidimensional de forma `(100,1)`. Aplicamos la función `sin()` a esta matriz y agregamos una segunda onda sinusoidal obtenida multiplicando la matriz por 6. Luego agregamos algo de ruido gaussiano con una media de 0 y una desviación estándar de 0.1 usando la función `normal()` de Numpy.

```python
import numpy as np

rng = np.random.RandomState(1)
X = np.linspace(0, 6, 100)[:, np.newaxis]
y = np.sin(X).ravel() + np.sin(6 * X).ravel() + rng.normal(0, 0.1, X.shape[0])
```
