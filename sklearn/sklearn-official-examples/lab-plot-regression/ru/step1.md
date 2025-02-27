# Генерация выборочных данных

Сначала мы генерируем выборочные данные для нашей задачи регрессии. Мы создаем массив из 40 данных с 1 признаком, а затем создаем целевой массив, применяя функцию синуса к данным. Также мы добавляем некоторый шум к каждому 5-му элементу данных.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors

np.random.seed(0)
X = np.sort(5 * np.random.rand(40, 1), axis=0)
T = np.linspace(0, 5, 500)[:, np.newaxis]
y = np.sin(X).ravel()

# Add noise to targets
y[::5] += 1 * (0.5 - np.random.rand(8))
```
