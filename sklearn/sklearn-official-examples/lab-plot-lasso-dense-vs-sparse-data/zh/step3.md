# 在密集数据上训练Lasso

现在我们训练两个Lasso回归模型，一个在密集数据上，另一个在稀疏数据上。我们将alpha参数设置为1，最大迭代次数设置为1000。

```python
alpha = 1
sparse_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=1000)
dense_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=1000)
```
