# Генерация данных

В этом шаге мы генерируем случайный набор данных с `n_samples` образцами и `n_features` признаками. Также мы добавляем несколько выбросов в набор данных.

```python
n_samples = 80
n_features = 5

# Generate random dataset
rng = np.random.RandomState(42)
X = rng.randn(n_samples, n_features)

# Add outliers to the dataset
n_outliers = 20
outliers_index = rng.permutation(n_samples)[:n_outliers]
outliers_offset = 10.0 * (
    np.random.randint(2, size=(n_outliers, n_features)) - 0.5
)
X[outliers_index] += outliers_offset
```
