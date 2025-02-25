# Генерировать тестовые точки данных

Мы генерируем набор случайных тестовых точек данных, с значениями x и y в диапазоне от -1 до 1. Мы также генерируем соответствующий набор значений z с использованием функции `experiment_res`, определенной на шаге 2.

```python
# User parameters for data test points

# Number of test data points, tested from 3 to 5000 for subdiv=3
n_test = 200

# Random points
random_gen = np.random.RandomState(seed=19680801)
x_test = random_gen.uniform(-1., 1., size=n_test)
y_test = random_gen.uniform(-1., 1., size=n_test)
z_test = experiment_res(x_test, y_test)
```
