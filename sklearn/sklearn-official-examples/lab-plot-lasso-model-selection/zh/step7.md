# 通过坐标下降法实现的套索回归

我们将使用 `LassoCV` 进行超参数调整。

```python
from sklearn.linear_model import LassoCV

start_time = time.time()
model = make_pipeline(StandardScaler(), LassoCV(cv=20)).fit(X, y)
fit_time = time.time() - start_time
```
