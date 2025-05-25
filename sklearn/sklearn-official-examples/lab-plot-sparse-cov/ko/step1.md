# 데이터 생성

첫 번째 단계는 데이터를 생성하는 것입니다. 이 경우 20 개의 특징을 가진 60 개의 샘플로 구성된 작은 데이터셋을 생성합니다. 유리한 복구 조건을 보장하기 위해 희소 역공분산 행렬을 사용합니다.

```python
import numpy as np
from scipy import linalg
from sklearn.datasets import make_sparse_spd_matrix

n_samples = 60
n_features = 20

prng = np.random.RandomState(1)
prec = make_sparse_spd_matrix(
    n_features, alpha=0.98, smallest_coef=0.4, largest_coef=0.7, random_state=prng
)
cov = linalg.inv(prec)
d = np.sqrt(np.diag(cov))
cov /= d
cov /= d[:, np.newaxis]
prec *= d
prec *= d[:, np.newaxis]
X = prng.multivariate_normal(np.zeros(n_features), cov, size=n_samples)
X -= X.mean(axis=0)
X /= X.std(axis=0)
```
