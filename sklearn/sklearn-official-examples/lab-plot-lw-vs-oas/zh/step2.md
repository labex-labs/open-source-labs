# 生成数据

接下来，我们将生成具有遵循自回归（AR(1)）过程的协方差矩阵的高斯分布数据。我们将使用 `scipy.linalg` 中的 `toeplitz` 和 `cholesky` 函数来生成协方差矩阵。

```python
np.random.seed(0)

n_features = 100
r = 0.1
real_cov = toeplitz(r ** np.arange(n_features))
coloring_matrix = cholesky(real_cov)
```
