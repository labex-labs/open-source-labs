# Генерация примерных данных

Мы сгенерируем примерные данные с использованием функции `make_regression()` из Scikit-learn. Мы установим количество тренировочных образцов в 75, количество тестовых образцов в 150 и количество признаков в 500. Мы также установим `n_informative` в 50 и `shuffle` в False.

```python
import numpy as np
from sklearn import linear_model
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

n_samples_train, n_samples_test, n_features = 75, 150, 500
X, y, coef = make_regression(
    n_samples=n_samples_train + n_samples_test,
    n_features=n_features,
    n_informative=50,
    shuffle=False,
    noise=1.0,
    coef=True,
)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=n_samples_train, test_size=n_samples_test, shuffle=False
)
```
