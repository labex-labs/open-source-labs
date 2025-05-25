# 데이터 다운로드 및 누락 값 세트 생성

먼저 두 데이터 세트를 다운로드합니다. 계산 속도를 높이기 위해 캘리포니아 주택 데이터 세트의 처음 400 개 항목만 사용할 것입니다. 그런 다음 일부 값을 제거하여 인위적으로 누락된 데이터가 있는 새로운 버전을 생성합니다.

```python
import numpy as np
from sklearn.datasets import fetch_california_housing, load_diabetes

rng = np.random.RandomState(42)

X_diabetes, y_diabetes = load_diabetes(return_X_y=True)
X_california, y_california = fetch_california_housing(return_X_y=True)
X_california = X_california[:400]
y_california = y_california[:400]
X_diabetes = X_diabetes[:400]
y_diabetes = y_diabetes[:400]

def add_missing_values(X_full, y_full):
    n_samples, n_features = X_full.shape

    # 75% 의 행에 누락 값 추가
    missing_rate = 0.75
    n_missing_samples = int(n_samples * missing_rate)

    missing_samples = np.zeros(n_samples, dtype=bool)
    missing_samples[:n_missing_samples] = True

    rng.shuffle(missing_samples)
    missing_features = rng.randint(0, n_features, n_missing_samples)
    X_missing = X_full.copy()
    X_missing[missing_samples, missing_features] = np.nan
    y_missing = y_full.copy()

    return X_missing, y_missing

X_miss_california, y_miss_california = add_missing_values(X_california, y_california)
X_miss_diabetes, y_miss_diabetes = add_missing_values(X_diabetes, y_diabetes)
```
