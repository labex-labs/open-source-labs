# MeanShift 알고리즘을 이용한 클러스터링

이제 `sklearn.cluster` 모듈의 `MeanShift` 클래스를 사용하여 Mean-Shift 알고리즘으로 클러스터링을 수행합니다. `estimate_bandwidth` 함수를 사용하여 각 점의 영향력 범위를 나타내는 밴드위스 (bandwidth) 매개변수를 자동으로 감지합니다.

```python
bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=500)
ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
ms.fit(X)
labels = ms.labels_
cluster_centers = ms.cluster_centers_
```
