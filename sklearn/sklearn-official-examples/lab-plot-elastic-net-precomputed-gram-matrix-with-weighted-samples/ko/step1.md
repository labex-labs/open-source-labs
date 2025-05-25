# 데이터셋 로드 및 샘플 가중치 생성

데이터셋을 로드하고 샘플 가중치를 생성하는 것으로 시작합니다. scikit-learn 의 `make_regression` 함수를 사용하여 100,000 개의 샘플을 가진 랜덤 회귀 데이터셋을 생성합니다. 그런 다음 로그정규 가중치 벡터를 생성하고, 이를 정규화하여 총 샘플 수에 합산되도록 합니다.

```python
import numpy as np
from sklearn.datasets import make_regression

rng = np.random.RandomState(0)

n_samples = int(1e5)
X, y = make_regression(n_samples=n_samples, noise=0.5, random_state=rng)

sample_weight = rng.lognormal(size=n_samples)
# 샘플 가중치를 정규화합니다.
normalized_weights = sample_weight * (n_samples / (sample_weight.sum()))
```
