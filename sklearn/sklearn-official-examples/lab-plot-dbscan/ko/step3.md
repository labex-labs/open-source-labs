# DBSCAN 클러스터링 계산

sklearn.cluster 모듈의 DBSCAN 클래스를 사용하여 클러스터를 계산합니다. eps 매개변수를 0.3 으로, min_samples 매개변수를 10 으로 설정합니다. DBSCAN 이 할당한 레이블은 labels\_ 속성을 통해 접근할 수 있습니다. 노이즈 샘플은 레이블 -1 을 받습니다. 또한, 클러스터 개수와 노이즈 포인트 개수를 계산합니다.

```python
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics

db = DBSCAN(eps=0.3, min_samples=10).fit(X)
labels = db.labels_

n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

print("Estimated number of clusters: %d" % n_clusters_)
print("Estimated number of noise points: %d" % n_noise_)
```
