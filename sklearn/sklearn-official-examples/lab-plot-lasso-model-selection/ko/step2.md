# 랜덤 특징 추가

Lasso 모델이 수행하는 특징 선택을 더 잘 보여주기 위해 원본 데이터에 몇 가지 랜덤 특징을 추가합니다. 랜덤 특징은 `numpy`의 `RandomState` 함수를 사용하여 생성됩니다.

```python
import numpy as np
import pandas as pd

rng = np.random.RandomState(42)
n_random_features = 14
X_random = pd.DataFrame(
    rng.randn(X.shape[0], n_random_features),
    columns=[f"random_{i:02d}" for i in range(n_random_features)],
)
X = pd.concat([X, X_random], axis=1)
X[X.columns[::3]].head()
```
