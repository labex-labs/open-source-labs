# Métricas de Distância

As métricas de distância são funções que medem a dissimilaridade entre dois objetos. Estas métricas satisfazem certas condições, como não negatividade, simetria e a desigualdade triangular.

Algumas métricas de distância populares incluem a distância euclidiana, a distância de Manhattan e a distância de Minkowski.

Vamos calcular as distâncias em pares entre dois conjuntos de amostras usando a função `pairwise_distances`:

```python
import numpy as np
from sklearn.metrics import pairwise_distances

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# Calcular as distâncias em pares entre X e Y
distances = pairwise_distances(X, Y, metric='manhattan')
print(distances)
```

Saída:

```
array([[4., 2.],
       [7., 5.],
       [12., 10.]])
```
