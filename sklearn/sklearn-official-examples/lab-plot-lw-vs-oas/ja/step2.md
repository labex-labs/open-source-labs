# データの生成

次に、AR(1) 過程に従う共分散行列を持つガウス分布データを生成します。共分散行列を生成するために、`scipy.linalg` からの `toeplitz` 関数と `cholesky` 関数を使用します。

```python
np.random.seed(0)

n_features = 100
r = 0.1
real_cov = toeplitz(r ** np.arange(n_features))
coloring_matrix = cholesky(real_cov)
```
