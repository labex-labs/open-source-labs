# Генерация данных

Мы генерируем две компоненты (каждая из которых содержит `n_samples`), случайным образом выбирая из стандартного нормального распределения, возвращаемого функцией `numpy.random.randn`. Одна компонента остаётся сферической, но сдвинутой и перемасштабированной. Другая деформируется, чтобы иметь более общий матрицу ковариации.

```python
import numpy as np

n_samples = 500
np.random.seed(0)
C = np.array([[0.0, -0.1], [1.7, 0.4]])
component_1 = np.dot(np.random.randn(n_samples, 2), C)  # general
component_2 = 0.7 * np.random.randn(n_samples, 2) + np.array([-4, 1])  # spherical

X = np.concatenate([component_1, component_2])
```
