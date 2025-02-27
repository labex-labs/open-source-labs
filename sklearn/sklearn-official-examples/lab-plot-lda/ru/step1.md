# Генерация случайных данных

Во - первых, нам нужно сгенерировать случайные данные с дискриминативной характеристикой и шумовыми характеристиками. Мы будем использовать функцию `make_blobs` из scikit - learn для генерации двух кластеров данных с одной дискриминативной характеристикой. Затем мы добавим случайный шум к другим характеристикам.

```python
import numpy as np
from sklearn.datasets import make_blobs

def generate_data(n_samples, n_features):
    """Generate random blob-ish data with noisy features.

    This returns an array of input data with shape `(n_samples, n_features)`
    and an array of `n_samples` target labels.

    Only one feature contains discriminative information, the other features
    contain only noise.
    """
    X, y = make_blobs(n_samples=n_samples, n_features=1, centers=[[-2], [2]])

    # add non-discriminative features
    if n_features > 1:
        X = np.hstack([X, np.random.randn(n_samples, n_features - 1)])
    return X, y
```
