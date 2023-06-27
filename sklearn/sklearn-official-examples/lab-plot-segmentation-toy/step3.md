# Spectral clustering

We will use the `spectral_clustering` function from `sklearn.cluster` to perform spectral clustering. The `n_clusters` parameter is set to 4 to separate the four circles.

```python
from sklearn.cluster import spectral_clustering

labels = spectral_clustering(graph, n_clusters=4, eigen_solver="arpack")
```
