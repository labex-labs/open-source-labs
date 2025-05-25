# KMeans 를 이용한 클러스터링

KMeans 를 이용하여 클러스터링을 수행합니다.

```python
import time
from sklearn.cluster import KMeans

k_means = KMeans(init="k-means++", n_clusters=3, n_init=10)
t0 = time.time()
k_means.fit(X)
t_batch = time.time() - t0
```
