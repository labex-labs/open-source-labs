# Lasso a través de la regresión de ángulo mínimo

Realizaremos la optimización de hiperparámetros utilizando `LassoLarsCV`.

```python
from sklearn.linear_model import LassoLarsCV

start_time = time.time()
model = make_pipeline(StandardScaler(), LassoLarsCV(cv=20)).fit(X, y)
fit_time = time.time() - start_time
```
