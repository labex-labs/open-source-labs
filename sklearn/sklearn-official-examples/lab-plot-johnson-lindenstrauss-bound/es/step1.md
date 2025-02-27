# Límites teóricos

El primer paso es explorar los límites teóricos del lema de Johnson-Lindenstrauss. Graficaremos el número mínimo de dimensiones necesario para garantizar una incrustación de `eps` para un número creciente de muestras `n_samples`. La distorsión introducida por una proyección aleatoria `p` se afirma por el hecho de que `p` está definiendo una incrustación de `eps` con buena probabilidad como se define por:

`(1 - eps) \|u - v\|^2 < \|p(u) - p(v)\|^2 < (1 + eps) \|u - v\|^2`

Donde `u` y `v` son cualquier fila tomada de un conjunto de datos de forma `(n_samples, n_features)` y `p` es una proyección por una matriz gaussiana aleatoria `N(0, 1)` de forma `(n_components, n_features)` (o una matriz esparsa de Achlioptas).

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.random_projection import johnson_lindenstrauss_min_dim

# rango de distorsiones admisibles
eps_range = np.linspace(0.1, 0.99, 5)
colors = plt.cm.Blues(np.linspace(0.3, 1.0, len(eps_range)))

# rango de número de muestras (observaciones) a incrustar
n_samples_range = np.logspace(1, 9, 9)

plt.figure()
for eps, color in zip(eps_range, colors):
    min_n_components = johnson_lindenstrauss_min_dim(n_samples_range, eps=eps)
    plt.loglog(n_samples_range, min_n_components, color=color)

plt.legend([f"eps = {eps:0.1f}" for eps in eps_range], loc="lower right")
plt.xlabel("Número de observaciones para incrustar eps")
plt.ylabel("Número mínimo de dimensiones")
plt.title("Límites de Johnson-Lindenstrauss:\nn_samples vs n_components")
plt.show()
```
