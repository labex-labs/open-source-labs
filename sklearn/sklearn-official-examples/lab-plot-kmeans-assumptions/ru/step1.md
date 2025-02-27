# Генерация данных

Мы будем использовать функцию `make_blobs` из scikit - learn для генерации различных наборов данных с различными распределениями. В следующем блоке кода мы генерируем четыре набора данных:

- Смесь гауссовых кластеров
- Анизотропно распределенные кластеры
- Кластеры с различной дисперсией
- Кластеры с различными размерами

```python
import numpy as np
from sklearn.datasets import make_blobs

n_samples = 1500
random_state = 170
transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]

X, y = make_blobs(n_samples=n_samples, random_state=random_state)
X_aniso = np.dot(X, transformation)  # Анизотропные кластеры
X_varied, y_varied = make_blobs(
    n_samples=n_samples, cluster_std=[1.0, 2.5, 0.5], random_state=random_state
)  # Различная дисперсия
X_filtered = np.vstack(
    (X[y == 0][:500], X[y == 1][:100], X[y == 2][:10])
)  # Кластеры с различными размерами
y_filtered = [0] * 500 + [1] * 100 + [2] * 10
```
