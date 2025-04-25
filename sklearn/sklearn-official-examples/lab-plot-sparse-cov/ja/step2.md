# 共分散の推定

2 番目のステップは、共分散を推定することです。疎な精度行列を学習するために、GraphicalLassoCV を使用します。また、結果を Ledoit-Wolf 推定器と比較します。

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
