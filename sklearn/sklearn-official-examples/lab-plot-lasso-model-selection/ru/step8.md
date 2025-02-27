# Lasso с использованием наименьшего углового регрессии

Мы будем настраивать гиперпараметры с использованием `LassoLarsCV`.

```python
from sklearn.linear_model import LassoLarsCV

start_time = time.time()
model = make_pipeline(StandardScaler(), LassoLarsCV(cv=20)).fit(X, y)
fit_time = time.time() - start_time
```
