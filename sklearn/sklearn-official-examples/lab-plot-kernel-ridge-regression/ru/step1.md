# Генерация выборочных данных

Мы сгенерируем датасет, состоящий из синусоидальной целевой функции и сильного шума, добавленного к каждому пятому точке данных.

```python
import numpy as np

# Generate sample data
rng = np.random.RandomState(42)
X = 5 * rng.rand(10000, 1)
y = np.sin(X).ravel()

# Add noise to targets
y[::5] += 3 * (0.5 - rng.rand(X.shape[0] // 5))

X_plot = np.linspace(0, 5, 100000)[:, None]
```
