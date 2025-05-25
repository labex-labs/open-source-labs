# 라이브러리 가져오기 및 샘플 데이터 생성

필요한 라이브러리를 가져오고 scikit-learn 의 `make_blobs` 함수를 사용하여 샘플 데이터를 생성하는 것으로 시작합니다.

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn.mixture import GaussianMixture
from sklearn.utils.extmath import row_norms
from sklearn.datasets._samples_generator import make_blobs
from timeit import default_timer as timer

# 데이터 생성
X, y_true = make_blobs(n_samples=4000, centers=4, cluster_std=0.60, random_state=0)
X = X[:, ::-1]

n_samples = 4000
n_components = 4
x_squared_norms = row_norms(X, squared=True)
```
