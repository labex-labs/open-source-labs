# Генерация примерных данных

Мы будем использовать функцию `make_blobs` из библиотеки scikit-learn для генерации примерных данных. Эта функция генерирует изотропные гауссовы "куски" (blobs) для кластеризации. Мы сгенерируем 4000 образцов с 4 центрами.

```python
# Generate sample data
n_samples = 4000
n_components = 4

X, y_true = make_blobs(
    n_samples=n_samples, centers=n_components, cluster_std=0.60, random_state=0
)
X = X[:, ::-1]
```
