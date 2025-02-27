# Загрузка датасета и создание весов выборок

Начнем с загрузки датасета и создания некоторых весов выборок. Мы используем функцию `make_regression` из scikit - learn для генерации случайного датасета для регрессии с 100 000 выборками. Затем мы генерируем вектор весов, распределенных по логнормальному закону, и нормализуем его так, чтобы сумма составляла общее количество выборок.

```python
import numpy as np
from sklearn.datasets import make_regression

rng = np.random.RandomState(0)

n_samples = int(1e5)
X, y = make_regression(n_samples=n_samples, noise=0.5, random_state=rng)

sample_weight = rng.lognormal(size=n_samples)
# normalize the sample weights
normalized_weights = sample_weight * (n_samples / (sample_weight.sum()))
```
