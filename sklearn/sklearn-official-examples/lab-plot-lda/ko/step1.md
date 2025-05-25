# 랜덤 데이터 생성

먼저, 구별 가능한 특징과 잡음 특징을 가진 랜덤 데이터를 생성해야 합니다. scikit-learn 의 `make_blobs` 함수를 사용하여 하나의 구별 가능한 특징을 가진 두 개의 데이터 클러스터를 생성합니다. 그런 다음 다른 특징에 랜덤 노이즈를 추가합니다.

```python
import numpy as np
from sklearn.datasets import make_blobs

def generate_data(n_samples, n_features):
    """구별 가능한 특징과 잡음 특징을 가진 랜덤 데이터를 생성합니다.

    이 함수는 `(n_samples, n_features)` 모양의 입력 데이터 배열과 `n_samples` 개의 타겟 레이블 배열을 반환합니다.

    하나의 특징만 구별 가능한 정보를 포함하고, 다른 특징은 노이즈만 포함합니다.
    """
    X, y = make_blobs(n_samples=n_samples, n_features=1, centers=[[-2], [2]])

    # 구별 불가능한 특징 추가
    if n_features > 1:
        X = np.hstack([X, np.random.randn(n_samples, n_features - 1)])
    return X, y
```
