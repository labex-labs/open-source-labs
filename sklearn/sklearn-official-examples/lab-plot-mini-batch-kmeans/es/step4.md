# Estableciendo la paridad entre los clusters

Queremos que el mismo cluster tenga el mismo color tanto con el algoritmo MiniBatchKMeans como con KMeans. Vamos a emparejar los centros de los clusters por el más cercano.

```python
from sklearn.metrics.pairwise import pairwise_distances_argmin

k_means_cluster_centers = k_means.cluster_centers_
order = pairwise_distances_argmin(k_means.cluster_centers_, mbk.cluster_centers_)
mbk_means_cluster_centers = mbk.cluster_centers_[order]

k_means_labels = pairwise_distances_argmin(X, k_means_cluster_centers)
mbk_means_labels = pairwise_distances_argmin(X, mbk_means_cluster_centers)
```
