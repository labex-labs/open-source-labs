# Импортируем библиотеки и генерируем датасет

Сначала импортируем необходимые библиотеки и сгенерируем синтетический датасет для анализа регрессии.

```python
import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, TheilSenRegressor
from sklearn.linear_model import RANSACRegressor

np.random.seed(0)
n_samples = 200
x = np.random.randn(n_samples)
w = 3.0
c = 2.0
noise = 0.1 * np.random.randn(n_samples)
y = w * x + c + noise
X = x[:, np.newaxis]
```
