# Agrupamiento espectral

Usaremos la función `spectral_clustering` de `sklearn.cluster` para realizar el agrupamiento espectral. El parámetro `n_clusters` se establece en 4 para separar los cuatro círculos.

```python
from sklearn.cluster import spectral_clustering

labels = spectral_clustering(graph, n_clusters=4, eigen_solver="arpack")
```
