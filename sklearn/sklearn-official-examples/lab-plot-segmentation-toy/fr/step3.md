# Classification spectrale

Nous allons utiliser la fonction `spectral_clustering` de `sklearn.cluster` pour effectuer une classification spectrale. Le paramètre `n_clusters` est défini sur 4 pour séparer les quatre cercles.

```python
from sklearn.cluster import spectral_clustering

labels = spectral_clustering(graph, n_clusters=4, eigen_solver="arpack")
```
