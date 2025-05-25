# OPTICS 군집화 알고리즘 실행

이제 생성된 데이터에 OPTICS 군집화 알고리즘을 적용합니다. 이 예제에서는 `min_samples=50`, `xi=0.05`, `min_cluster_size=0.05`로 설정합니다.

```python
clust = OPTICS(min_samples=50, xi=0.05, min_cluster_size=0.05)
clust.fit(X)
```
