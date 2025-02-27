# Загрузка набора данных о диабете

Сначала мы загружаем набор данных о диабете из scikit-learn и разделяем его на обучающую и тестовую выборки.

```python
from sklearn import datasets
import numpy as np

X, y = datasets.load_diabetes(return_X_y=True)
indices = (0, 1)

X_train = X[:-20, indices]
X_test = X[-20:, indices]
y_train = y[:-20]
y_test = y[-20:]
```
