# Генерация данных

Во - первых, мы генерируем набор данных из 125 выборок и 2 признаков. Оба признака распределены по Гауссу с математическим ожиданием 0. Однако, для признака 1 стандартное отклонение равно 2, а для признака 2 стандартное отклонение равно 1. Далее, мы заменяем 25 выборок на гауссовские выборки с выбросами, где для признака 1 стандартное отклонение равно 1, а для признака 2 стандартное отклонение равно 7.

```python
import numpy as np

# для совместимости результатов
np.random.seed(7)

n_samples = 125
n_outliers = 25
n_features = 2

# генерируем гауссовские данные формы (125, 2)
gen_cov = np.eye(n_features)
gen_cov[0, 0] = 2.0
X = np.dot(np.random.randn(n_samples, n_features), gen_cov)
# добавляем некоторые выбросы
outliers_cov = np.eye(n_features)
outliers_cov[np.arange(1, n_features), np.arange(1, n_features)] = 7.0
X[-n_outliers:] = np.dot(np.random.randn(n_outliers, n_features), outliers_cov)
```
