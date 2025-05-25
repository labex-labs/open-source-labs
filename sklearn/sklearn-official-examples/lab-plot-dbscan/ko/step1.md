# 데이터 생성

sklearn.datasets 모듈의 make_blobs 함수를 사용하여 세 개의 클러스터를 가진 합성 데이터셋을 생성합니다. 이 데이터셋은 750 개의 샘플로 구성되며, 클러스터 표준 편차는 0.4 입니다. 또한 sklearn.preprocessing 모듈의 StandardScaler 를 사용하여 데이터를 표준화합니다.

```python
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(
    n_samples=750, centers=centers, cluster_std=0.4, random_state=0
)

X = StandardScaler().fit_transform(X)
```
