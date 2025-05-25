# 데이터 로드 및 준비

먼저, Scikit-learn 라이브러리를 사용하여 아이리스 데이터셋을 로드합니다. 아이리스 데이터셋은 3 개의 아이리스 식물 종류를 포함하며, 하나의 종류를 제거하여 이진 분류 문제를 생성하여 데이터셋을 이진화합니다. 또한 문제를 더 어렵게 하기 위해 노이즈가 있는 특징을 추가합니다.

```python
import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()
target_names = iris.target_names
X, y = iris.data, iris.target
X, y = X[y != 2], y[y != 2]
n_samples, n_features = X.shape

# 노이즈 특징 추가
random_state = np.random.RandomState(0)
X = np.concatenate([X, random_state.randn(n_samples, 200 * n_features)], axis=1)
```
