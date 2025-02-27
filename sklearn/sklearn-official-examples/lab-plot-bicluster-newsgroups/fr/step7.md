# Effectuer un clustering avec MiniBatchKMeans

Nous allons effectuer un clustering des données à l'aide de MiniBatchKMeans.

```python
kmeans = MiniBatchKMeans(
    n_clusters=len(categories), batch_size=20000, random_state=0, n_init=3
)
y_kmeans = kmeans.fit_predict(X)
```
