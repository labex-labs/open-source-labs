# 在稀疏数据上训练 Lasso

现在我们训练两个 Lasso 回归模型，一个在密集数据上，另一个在稀疏数据上。我们将 alpha 参数设置为 0.1，最大迭代次数设置为 10000。

```python
alpha = 0.1
sparse_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=10000)
dense_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=10000)
```
