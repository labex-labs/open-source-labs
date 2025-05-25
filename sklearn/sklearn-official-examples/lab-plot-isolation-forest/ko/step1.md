# 데이터 생성

두 개의 클러스터와 몇 개의 이상치를 포함하는 데이터셋을 생성합니다. 클러스터는 표준 정규 분포에서 무작위로 샘플링하여 생성됩니다. 하나는 구형이고 다른 하나는 약간 변형된 형태입니다. 이상치는 균일 분포에서 무작위로 샘플링하여 생성합니다.

```python
import numpy as np
from sklearn.model_selection import train_test_split

n_samples, n_outliers = 120, 40
rng = np.random.RandomState(0)
covariance = np.array([[0.5, -0.1], [0.7, 0.4]])
cluster_1 = 0.4 * rng.randn(n_samples, 2) @ covariance + np.array([2, 2])  # 일반적인 형태
cluster_2 = 0.3 * rng.randn(n_samples, 2) + np.array([-2, -2])  # 구형
outliers = rng.uniform(low=-4, high=4, size=(n_outliers, 2))

X = np.concatenate([cluster_1, cluster_2, outliers])
y = np.concatenate(
    [np.ones((2 * n_samples), dtype=int), -np.ones((n_outliers), dtype=int)]
)

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)
```
