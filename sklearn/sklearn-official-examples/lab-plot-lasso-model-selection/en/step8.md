# Lasso via Least Angle Regression

We will make the hyperparameter tuning using `LassoLarsCV`.

```python
from sklearn.linear_model import LassoLarsCV

start_time = time.time()
model = make_pipeline(StandardScaler(), LassoLarsCV(cv=20)).fit(X, y)
fit_time = time.time() - start_time
```
