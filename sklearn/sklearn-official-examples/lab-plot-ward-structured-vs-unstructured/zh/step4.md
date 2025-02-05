# 结构化层次聚类

我们使用 Scikit-learn 中的 `kneighbors_graph` 函数定义具有 10 个邻居的 k 近邻。

```python
from sklearn.neighbors import kneighbors_graph

connectivity = kneighbors_graph(X, n_neighbors=10, include_self=False)
```

我们再次执行具有连接性约束的凝聚聚类。

```python
ward = AgglomerativeClustering(
    n_clusters=6, connectivity=connectivity, linkage="ward"
).fit(X)
label = ward.labels_
```
