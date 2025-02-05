# 定义聚类数和算法

在这一步中，我们将定义 KMeans 和二分 KMeans 的聚类中心数量。我们还将定义要比较的算法。

```python
n_clusters_list = [4, 8, 16]
clustering_algorithms = {
    "Bisecting K-Means": BisectingKMeans,
    "K-Means": KMeans,
}
```
