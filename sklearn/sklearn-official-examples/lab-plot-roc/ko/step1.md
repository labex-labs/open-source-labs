# 데이터 로드 및 준비

ROC 지표를 사용하여 분류기의 성능을 평가하기 위해 아이리스 데이터셋을 로드하고 준비하는 방법을 살펴봅니다.

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
target_names = iris.target_names
X, y = iris.data, iris.target
y = iris.target_names[y]

# 문제를 더 어렵게 하기 위해 노이즈 특징 추가
random_state = np.random.RandomState(0)
n_samples, n_features = X.shape
n_classes = len(np.unique(y))
X = np.concatenate([X, random_state.randn(n_samples, 200 * n_features)], axis=1)

# 데이터를 학습 및 테스트 세트로 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, stratify=y, random_state=0)
```
