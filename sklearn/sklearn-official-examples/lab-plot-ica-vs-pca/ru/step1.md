# Генерация выборочных данных

В этом шаге мы генерируем выборочные данные с использованием высоко негауссового процесса, 2-мерного распределения Стьюдента с малым числом степеней свободы.

```python
import numpy as np

from sklearn.decomposition import PCA, FastICA

rng = np.random.RandomState(42)
S = rng.standard_t(1.5, size=(20000, 2))
S[:, 0] *= 2.0

# Mix data
A = np.array([[1, 1], [0, 2]])  # Mixing matrix

X = np.dot(S, A.T)  # Generate observations
```
