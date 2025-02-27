# Загрузка набора данных

Начнем с загрузки набора данных с рукописными цифрами с использованием функции `load_digits()` из scikit-learn. Эта функция возвращает признаки и метки для набора данных.

```python
import numpy as np
from sklearn.datasets import load_digits

data, labels = load_digits(return_X_y=True)
(n_samples, n_features), n_digits = data.shape, np.unique(labels).size
```
