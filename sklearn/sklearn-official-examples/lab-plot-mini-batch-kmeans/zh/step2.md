# 使用 KMeans 进行聚类计算

我们将使用 KMeans 进行聚类计算。

```python
import time
from sklearn.cluster import KMeans

k_means = KMeans(init="k-means++", n_clusters=3, n_init=10)
t0 = time.time()
k_means.fit(X)
t_batch = time.time() - t0
```
