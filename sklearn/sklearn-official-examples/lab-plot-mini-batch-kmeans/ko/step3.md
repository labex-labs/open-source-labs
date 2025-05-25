# MiniBatchKMeans 를 이용한 클러스터링

MiniBatchKMeans 를 이용하여 클러스터링을 수행합니다.

```python
from sklearn.cluster import MiniBatchKMeans

mbk = MiniBatchKMeans(
    init="k-means++",
    n_clusters=3,
    batch_size=batch_size,
    n_init=10,
    max_no_improvement=10,
    verbose=0,
)
t0 = time.time()
mbk.fit(X)
t_mini_batch = time.time() - t0
```
