# Генерируем игрушечные данные

Теперь мы сгенерируем игрушечный набор данных с использованием функции make_regression из scikit - learn. Мы сгенерируем набор данных с 20 выборками, одним признаком и случайным种子ом 0. Также мы добавим некоторый шум к набору данных.

```python
rng = np.random.RandomState(0)
X, y = make_regression(
    n_samples=20, n_features=1, random_state=0, noise=4.0, bias=100.0
)
```
