# Mesures de distance

Les mesures de distance sont des fonctions qui mesurent la dissimilarité entre deux objets. Ces mesures satisfont certaines conditions, telles que la non-négativité, la symétrie et l'inégalité triangulaire.

Certaines mesures de distance populaires incluent la distance euclidienne, la distance de Manhattan et la distance de Minkowski.

Calculons les distances entre paires de deux ensembles d'échantillons à l'aide de la fonction `pairwise_distances` :

```python
import numpy as np
from sklearn.metrics import pairwise_distances

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# Calculate pairwise distances between X and Y
distances = pairwise_distances(X, Y, metric='manhattan')
print(distances)
```

Sortie :

```
array([[4., 2.],
       [7., 5.],
       [12., 10.]])
```
