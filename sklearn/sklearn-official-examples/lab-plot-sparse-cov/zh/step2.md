# 估计协方差

第二步是估计协方差。我们使用图形拉索交叉验证（GraphicalLassoCV）来学习稀疏精度矩阵。我们还将结果与莱杜瓦-沃尔夫（Ledoit-Wolf）估计器进行比较。

```python
from sklearn.covariance import GraphicalLassoCV, ledoit_wolf

emp_cov = np.dot(X.T, X) / n_samples

model = GraphicalLassoCV()
model.fit(X)
cov_ = model.covariance_
prec_ = model.precision_

lw_cov_, _ = ledoit_wolf(X)
lw_prec_ = linalg.inv(lw_cov_)
```
