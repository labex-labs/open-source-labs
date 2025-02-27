# Lasso über Koordinatenabstieg

Wir werden die Hyperparameteroptimierung mit `LassoCV` vornehmen.

```python
from sklearn.linear_model import LassoCV

start_time = time.time()
model = make_pipeline(StandardScaler(), LassoCV(cv=20)).fit(X, y)
fit_time = time.time() - start_time
```
