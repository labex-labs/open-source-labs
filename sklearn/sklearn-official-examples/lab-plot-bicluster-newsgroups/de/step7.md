# Clustern mit MiniBatchKMeans

Wir werden die Daten mit MiniBatchKMeans clustern.

```python
kmeans = MiniBatchKMeans(
    n_clusters=len(categories), batch_size=20000, random_state=0, n_init=3
)
y_kmeans = kmeans.fit_predict(X)
```
