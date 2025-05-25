# 스펙트럴 공동 클러스터링 알고리즘을 이용한 이분 클러스터링

스펙트럴 공동 클러스터링 알고리즘을 사용하여 이분 클러스터링을 수행합니다. 공동 클러스터 객체를 정의하고 데이터에 맞춥니다.

```python
cocluster = SpectralCoclustering(
    n_clusters=len(categories), svd_method="arpack", random_state=0
)
cocluster.fit(X)
y_cocluster = cocluster.row_labels_
```
