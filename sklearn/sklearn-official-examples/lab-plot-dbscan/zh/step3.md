# 计算 DBSCAN

我们将使用 `sklearn.cluster` 模块中的 `DBSCAN` 类来计算聚类。我们将把 `eps` 参数设置为 0.3，把 `min_samples` 参数设置为 10。我们可以使用 `labels_` 属性来获取由 DBSCAN 分配的标签。噪声样本被赋予标签 -1。我们还将计算聚类的数量和噪声点的数量。

```python
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics

db = DBSCAN(eps=0.3, min_samples=10).fit(X)
labels = db.labels_

n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

print("Estimated number of clusters: %d" % n_clusters_)
print("Estimated number of noise points: %d" % n_noise_)
```
