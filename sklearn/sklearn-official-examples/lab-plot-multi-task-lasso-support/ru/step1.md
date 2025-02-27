# Генерация данных

Во - первых, нам нужно сгенерировать некоторые образцы данных, которые мы сможем использовать для подгонки наших моделей. Мы будем использовать numpy для генерации 100 образцов, каждый из которых имеет 30 признаков и 40 задач. Также мы случайным образом выберем 5 значимых признаков и создадим для них коэффициенты с использованием синусоид с случайной частотой и фазой. Наконец, мы добавим некоторый случайный шум к данным.

```python
import numpy as np

rng = np.random.RandomState(42)

# Generate some 2D coefficients with sine waves with random frequency and phase
n_samples, n_features, n_tasks = 100, 30, 40
n_relevant_features = 5
coef = np.zeros((n_tasks, n_features))
times = np.linspace(0, 2 * np.pi, n_tasks)
for k in range(n_relevant_features):
    coef[:, k] = np.sin((1.0 + rng.randn(1)) * times + 3 * rng.randn(1))

X = rng.randn(n_samples, n_features)
Y = np.dot(X, coef.T) + rng.randn(n_samples, n_tasks)
```
