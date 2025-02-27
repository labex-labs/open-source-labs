# Добавляем сильные выбросы в набор данных

Мы добавим четыре сильных выброса в набор данных. Мы сгенерируем случайные значения для этих выбросов с использованием нормального распределения. Затем мы добавим эти выбросы в набор данных.

```python
X_outliers = rng.normal(0, 0.5, size=(4, 1))
y_outliers = rng.normal(0, 2.0, size=4)
X_outliers[:2, :] += X.max() + X.mean() / 4.0
X_outliers[2:, :] += X.min() - X.mean() / 4.0
y_outliers[:2] += y.min() - y.mean() / 4.0
y_outliers[2:] += y.max() + y.mean() / 4.0
X = np.vstack((X, X_outliers))
y = np.concatenate((y, y_outliers))
```
