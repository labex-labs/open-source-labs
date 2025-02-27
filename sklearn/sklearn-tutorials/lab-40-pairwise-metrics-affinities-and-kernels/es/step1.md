# Métricas de Distancia

Las métricas de distancia son funciones que miden la disimilitud entre dos objetos. Estas métricas cumplen ciertas condiciones, como no-negatividad, simetría y la desigualdad triangular.

Algunas métricas de distancia populares incluyen la distancia euclidiana, la distancia de Manhattan y la distancia de Minkowski.

Calculemos las distancias entre pares de dos conjuntos de muestras utilizando la función `pairwise_distances`:

```python
import numpy as np
from sklearn.metrics import pairwise_distances

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# Calculate pairwise distances between X and Y
distances = pairwise_distances(X, Y, metric='manhattan')
print(distances)
```

Salida:

```
array([[4., 2.],
       [7., 5.],
       [12., 10.]])
```
