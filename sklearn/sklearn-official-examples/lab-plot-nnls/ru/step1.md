# Генерация случайных данных

Мы сгенерируем некоторые случайные данные для тестирования нашего алгоритма. Мы создадим 200 выборок с 50 признаками и применим истинный коэффициент 3 для каждого признака. Затем мы установим порог для коэффициентов, чтобы сделать их неотрицательными. Наконец, мы добавим некоторый шум к выборкам.

```python
import numpy as np

np.random.seed(42)

n_samples, n_features = 200, 50
X = np.random.randn(n_samples, n_features)
true_coef = 3 * np.random.randn(n_features)
true_coef[true_coef < 0] = 0
y = np.dot(X, true_coef)
y += 5 * np.random.normal(size=(n_samples,))
```
