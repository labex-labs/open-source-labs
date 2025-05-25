# 데이터 로드

아이리스 데이터셋을 로드하고 36 개의 비정보 특징을 추가하여 시작합니다.

```python
import numpy as np
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

# 비정보 특징 추가
rng = np.random.RandomState(0)
X = np.hstack((X, 2 * rng.random((X.shape[0], 36))))
```
