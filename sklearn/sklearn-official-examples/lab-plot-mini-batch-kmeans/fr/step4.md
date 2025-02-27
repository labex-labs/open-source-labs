# Établissement de la parité entre les groupes

Nous souhaitons avoir la même couleur pour le même groupe avec les algorithmes MiniBatchKMeans et KMeans. Associons les centres de groupe les uns aux autres en fonction de la distance la plus courte.

```python
from sklearn.metrics.pairwise import pairwise_distances_argmin

k_means_cluster_centers = k_means.cluster_centers_
order = pairwise_distances_argmin(k_means.cluster_centers_, mbk.cluster_centers_)
mbk_means_cluster_centers = mbk.cluster_centers_[order]

k_means_labels = pairwise_distances_argmin(X, k_means_cluster_centers)
mbk_means_labels = pairwise_distances_argmin(X, mbk_means_cluster_centers)
```
