# 使用 MiniBatchKMeans 进行聚类

我们将使用 MiniBatchKMeans 对数据进行聚类。

```python
kmeans = MiniBatchKMeans(
    n_clusters=len(categories), batch_size=20000, random_state=0, n_init=3
)
y_kmeans = kmeans.fit_predict(X)
```
