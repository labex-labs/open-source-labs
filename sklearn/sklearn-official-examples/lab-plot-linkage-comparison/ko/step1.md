# 라이브러리 가져오기 및 데이터 로드

계층적 군집화 예제에 사용할 필요한 라이브러리를 가져오고 예제 데이터셋을 로드하는 것으로 시작합니다.

```python
import time
import warnings

import numpy as np
import matplotlib.pyplot as plt

from sklearn import cluster, datasets
from sklearn.preprocessing import StandardScaler
from itertools import cycle, islice

np.random.seed(0)

# %%
# 알고리즘의 확장성을 확인하기 위해 충분히 큰 크기의 데이터셋을 선택하지만, 너무 큰 크기로 인해 실행 시간이 너무 길어지지 않도록 합니다.

n_samples = 1500
noisy_circles = datasets.make_circles(n_samples=n_samples, factor=0.5, noise=0.05)
noisy_moons = datasets.make_moons(n_samples=n_samples, noise=0.05)
blobs = datasets.make_blobs(n_samples=n_samples, random_state=8)
no_structure = np.random.rand(n_samples, 2), None

# 이방성 분포 데이터
random_state = 170
X, y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
transformation = [[0.6, -0.6], [-0.4, 0.8]]
X_aniso = np.dot(X, transformation)
aniso = (X_aniso, y)

# 분산이 다른 blob 데이터
varied = datasets.make_blobs(
    n_samples=n_samples, cluster_std=[1.0, 2.5, 0.5], random_state=random_state
)
```
