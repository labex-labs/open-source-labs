# MiniBatchKMeans 를 이용한 클러스터링

MiniBatchKMeans 를 사용하여 데이터를 클러스터링합니다.

```python
kmeans = MiniBatchKMeans(
    n_clusters=len(categories), batch_size=20000, random_state=0, n_init=3
)
y_kmeans = kmeans.fit_predict(X)
```
