# Spectral Clustering

Wir werden die Funktion `spectral_clustering` aus `sklearn.cluster` verwenden, um spectral clustering durchzuführen. Der Parameter `n_clusters` wird auf 4 gesetzt, um die vier Kreise zu trennen.

```python
from sklearn.cluster import spectral_clustering

labels = spectral_clustering(graph, n_clusters=4, eigen_solver="arpack")
```
