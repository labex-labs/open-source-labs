# 最小角回帰による Lasso

`LassoLarsCV` を使用してハイパーパラメータのチューニングを行います。

```python
from sklearn.linear_model import LassoLarsCV

start_time = time.time()
model = make_pipeline(StandardScaler(), LassoLarsCV(cv=20)).fit(X, y)
fit_time = time.time() - start_time
```
