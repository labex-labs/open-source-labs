# 无结构层次聚类

我们执行凝聚聚类（AgglomerativeClustering），它属于无任何连接性约束的层次聚类。

```python
from sklearn.cluster import AgglomerativeClustering

ward = AgglomerativeClustering(n_clusters=6, linkage="ward").fit(X)
label = ward.labels_
```
