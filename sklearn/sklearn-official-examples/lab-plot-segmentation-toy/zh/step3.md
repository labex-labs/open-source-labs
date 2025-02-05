# 谱聚类

我们将使用 `sklearn.cluster` 中的 `spectral_clustering` 函数来执行谱聚类。`n_clusters` 参数设置为 4，以分离出四个圆圈。

```python
from sklearn.cluster import spectral_clustering

labels = spectral_clustering(graph, n_clusters=4, eigen_solver="arpack")
```
