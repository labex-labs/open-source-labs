# 구조적 계층적 군집화

Scikit-learn 의 `kneighbors_graph` 함수를 사용하여 10 개의 이웃을 갖는 k-최근접 이웃을 정의합니다.

```python
from sklearn.neighbors import kneighbors_graph

connectivity = kneighbors_graph(X, n_neighbors=10, include_self=False)
```

연결성 제약 조건을 다시 적용하여 AgglomerativeClustering 을 수행합니다.

```python
ward = AgglomerativeClustering(
    n_clusters=6, connectivity=connectivity, linkage="ward"
).fit(X)
label = ward.labels_
```
