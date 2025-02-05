# 通过最小角回归实现的套索回归

我们将使用 `LassoLarsCV` 进行超参数调整。

```python
from sklearn.linear_model import LassoLarsCV

start_time = time.time()
model = make_pipeline(StandardScaler(), LassoLarsCV(cv=20)).fit(X, y)
fit_time = time.time() - start_time
```
