# KMeans を使ったクラスタリングの計算

KMeans を使ってクラスタリングを計算します。

```python
import time
from sklearn.cluster import KMeans

k_means = KMeans(init="k-means++", n_clusters=3, n_init=10)
t0 = time.time()
k_means.fit(X)
t_batch = time.time() - t0
```
