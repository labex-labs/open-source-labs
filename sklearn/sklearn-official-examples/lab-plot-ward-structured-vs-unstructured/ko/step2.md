# 비구조적 계층적 군집화

연결 제약 조건 없이 계층적 군집화의 한 종류인 AgglomerativeClustering 을 수행합니다.

```python
from sklearn.cluster import AgglomerativeClustering

ward = AgglomerativeClustering(n_clusters=6, linkage="ward").fit(X)
label = ward.labels_
```
