# 스펙트럼 군집화

`sklearn.cluster`의 `spectral_clustering` 함수를 사용하여 스펙트럼 군집화를 수행합니다. `n_clusters` 매개변수를 4 로 설정하여 네 개의 원을 분리합니다.

```python
from sklearn.cluster import spectral_clustering

labels = spectral_clustering(graph, n_clusters=4, eigen_solver="arpack")
```
