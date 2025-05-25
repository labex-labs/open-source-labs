# Agrupamento espectral

Usaremos a função `spectral_clustering` de `sklearn.cluster` para realizar o agrupamento espectral. O parâmetro `n_clusters` é definido como 4 para separar os quatro círculos.

```python
from sklearn.cluster import spectral_clustering

labels = spectral_clustering(graph, n_clusters=4, eigen_solver="arpack")
```
