# Вычисление кластеризации с использованием KMeans

Мы вычислим кластеризацию с использованием KMeans.

```python
import time
from sklearn.cluster import KMeans

k_means = KMeans(init="k-means++", n_clusters=3, n_init=10)
t0 = time.time()
k_means.fit(X)
t_batch = time.time() - t0
```
