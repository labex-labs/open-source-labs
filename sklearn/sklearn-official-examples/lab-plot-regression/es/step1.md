# Generar datos de muestra

Primero generamos datos de muestra para utilizar en nuestro problema de regresión. Creamos una matriz de 40 puntos de datos con 1 característica, y luego creamos una matriz de objetivos aplicando la función seno a los datos. También agregamos algo de ruido a cada 5º punto de datos.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors

np.random.seed(0)
X = np.sort(5 * np.random.rand(40, 1), axis=0)
T = np.linspace(0, 5, 500)[:, np.newaxis]
y = np.sin(X).ravel()

# Add noise to targets
y[::5] += 1 * (0.5 - np.random.rand(8))
```
