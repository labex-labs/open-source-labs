# 필요한 라이브러리 가져오기 및 샘플 데이터 생성

먼저 필요한 라이브러리를 가져오고 샘플 데이터를 생성합니다. 세 개의 이차원 등방성 가우시안 분포의 혼합으로부터 데이터 세트를 생성합니다.

```python
import numpy as np
from sklearn.cluster import HDBSCAN, DBSCAN
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

centers = [[1, 1], [-1, -1], [1.5, -1.5]]
X, labels_true = make_blobs(n_samples=750, centers=centers, cluster_std=[0.4, 0.1, 0.75], random_state=0)
plt.scatter(X[:,0], X[:,1])
plt.show()
```
