# 데이터 생성

500 개의 샘플, 25 개의 특징, 랭크 5 를 갖는 가상 데이터셋을 생성할 것입니다. 또한, 동종 및 이종 노이즈를 데이터셋에 추가할 것입니다.

```python
import numpy as np
from scipy import linalg

n_samples, n_features, rank = 500, 25, 5
sigma = 1.0
rng = np.random.RandomState(42)
U, _, _ = linalg.svd(rng.randn(n_features, n_features))
X = np.dot(rng.randn(n_samples, rank), U[:, :rank].T)

# 동종 노이즈 추가
X_homo = X + sigma * rng.randn(n_samples, n_features)

# 이종 노이즈 추가
sigmas = sigma * rng.rand(n_features) + sigma / 2.0
X_hetero = X + rng.randn(n_samples, n_features) * sigmas
```
