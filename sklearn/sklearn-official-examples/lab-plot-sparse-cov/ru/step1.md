# Генерация данных

Первым шагом является генерация данных. В данном случае мы генерируем небольшой датасет из 60 выборок с 20 признаками. Мы используем разреженную обратную матрицу ковариации, чтобы обеспечить благоприятные условия восстановления.

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
