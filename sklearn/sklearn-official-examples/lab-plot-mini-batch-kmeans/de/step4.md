# Herstellen der Parität zwischen Clustern

Wir möchten die gleichen Cluster bei beiden Algorithmen, MiniBatchKMeans und KMeans, die gleiche Farbe haben. Ordnen wir die Clusterzentren anhand der nächsten Nachbarn zu.

```python
from sklearn.metrics.pairwise import pairwise_distances_argmin

k_means_cluster_centers = k_means.cluster_centers_
order = pairwise_distances_argmin(k_means.cluster_centers_, mbk.cluster_centers_)
mbk_means_cluster_centers = mbk.cluster_centers_[order]

k_means_labels = pairwise_distances_argmin(X, k_means_cluster_centers)
mbk_means_labels = pairwise_distances_argmin(X, mbk_means_cluster_centers)
```
