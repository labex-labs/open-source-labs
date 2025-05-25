# 샘플 데이터 생성

40 개의 특징과 20 개의 샘플을 가진 샘플 데이터를 생성합니다. `np.random.normal()` 함수를 사용하여 정규 분포를 생성합니다.

```python
import numpy as np

n_features, n_samples = 40, 20
np.random.seed(42)
base_X_train = np.random.normal(size=(n_samples, n_features))
base_X_test = np.random.normal(size=(n_samples, n_features))

coloring_matrix = np.random.normal(size=(n_features, n_features))
X_train = np.dot(base_X_train, coloring_matrix)
X_test = np.dot(base_X_test, coloring_matrix)
```
