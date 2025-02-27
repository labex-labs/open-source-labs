# Импортируем необходимые библиотеки и загружаем синтетические данные

Начнем с импорта необходимых библиотек и загрузки синтетических данных. Мы генерируем синтетический случайный датасет для регрессии и модифицируем целевые переменные, сдвигая все целевые значения так, чтобы все записи были неотрицательными, и применяя экспоненциальную функцию, чтобы получить нелинейные целевые переменные, которые нельзя подогнать с помощью простой линейной модели. Затем мы используем логарифмическую (np.log1p) и экспоненциальную функцию (np.expm1) для преобразования целевых переменных перед обучением модели линейной регрессии и ее использованием для предсказания.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.compose import TransformedTargetRegressor
from sklearn.linear_model import RidgeCV
from sklearn.metrics import median_absolute_error, r2_score, PredictionErrorDisplay

# Generate synthetic data
X, y = make_regression(n_samples=10_000, noise=100, random_state=0)

# Modify the targets
y = np.expm1((y + abs(y.min())) / 200)
y_trans = np.log1p(y)
```
