# 클러스터 간 동일성 확립

MiniBatchKMeans 와 KMeans 알고리즘에서 동일한 클러스터에 대해 동일한 색상을 사용하고자 합니다. 가장 가까운 클러스터 센터를 기준으로 페어링합니다.

```python
from sklearn.metrics.pairwise import pairwise_distances_argmin

k_means_cluster_centers = k_means.cluster_centers_
order = pairwise_distances_argmin(k_means.cluster_centers_, mbk.cluster_centers_)
mbk_means_cluster_centers = mbk.cluster_centers_[order]

k_means_labels = pairwise_distances_argmin(X, k_means_cluster_centers)
mbk_means_labels = pairwise_distances_argmin(X, mbk_means_cluster_centers)
```
