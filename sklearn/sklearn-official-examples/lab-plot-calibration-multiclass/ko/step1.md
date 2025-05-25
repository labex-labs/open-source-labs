# 데이터

2,000 개의 샘플, 2 개의 특징, 3 개의 목표 클래스를 가진 분류 데이터셋을 생성합니다. 다음과 같이 데이터를 분할합니다.

- train: 분류기를 학습하는 데 사용하는 600 개의 샘플
- valid: 예측 확률을 보정하는 데 사용하는 400 개의 샘플
- test: 1,000 개의 샘플

```python
import numpy as np
from sklearn.datasets import make_blobs

np.random.seed(0)

X, y = make_blobs(
    n_samples=2000, n_features=2, centers=3, random_state=42, cluster_std=5.0
)
X_train, y_train = X[:600], y[:600]
X_valid, y_valid = X[600:1000], y[600:1000]
X_train_valid, y_train_valid = X[:1000], y[:1000]
X_test, y_test = X[1000:], y[1000:]
```
