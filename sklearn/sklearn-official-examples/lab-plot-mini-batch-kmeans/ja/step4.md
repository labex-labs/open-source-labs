# クラスタ間の同等性の確立

MiniBatchKMeans と KMeans アルゴリズムの両方で、同じクラスタに同じ色を付けたいと思います。最も近いものごとにクラスタ中心をペアにしましょう。

```python
from sklearn.metrics.pairwise import pairwise_distances_argmin

k_means_cluster_centers = k_means.cluster_centers_
order = pairwise_distances_argmin(k_means.cluster_centers_, mbk.cluster_centers_)
mbk_means_cluster_centers = mbk.cluster_centers_[order]

k_means_labels = pairwise_distances_argmin(X, k_means_cluster_centers)
mbk_means_labels = pairwise_distances_argmin(X, mbk_means_cluster_centers)
```
