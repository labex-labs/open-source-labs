# K-Means 군집화 적용

이제 데이터에 K-Means 군집화 알고리즘을 적용할 것입니다. 알고리즘을 3 개의 클러스터로 초기화하고 데이터에 맞출 것입니다.

```python
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
```
