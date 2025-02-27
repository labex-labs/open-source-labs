# Генерация данных

Далее мы сгенерируем данные, распределенные нормально, с матрицей ковариации, которая подчиняется процессу AR(1). Мы будем использовать функции `toeplitz` и `cholesky` из `scipy.linalg` для генерации матрицы ковариации.

```python
np.random.seed(0)

n_features = 100
r = 0.1
real_cov = toeplitz(r ** np.arange(n_features))
coloring_matrix = cholesky(real_cov)
```
