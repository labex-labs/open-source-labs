# Загрузка набора данных

Мы загрузим набор данных о недвижимости в Калифорнии из Scikit-Learn. Мы будем использовать только 2000 образцов, чтобы сократить вычислительное время.

```python
N_SPLITS = 5

rng = np.random.RandomState(0)

X_full, y_full = fetch_california_housing(return_X_y=True)
X_full = X_full[::10]
y_full = y_full[::10]
n_samples, n_features = X_full.shape
```
