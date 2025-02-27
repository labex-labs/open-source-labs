# Kovarianz schätzen

Der zweite Schritt besteht darin, die Kovarianz zu schätzen. Wir verwenden GraphicalLassoCV, um die spärliche Präzisionsmatrix zu lernen. Wir vergleichen auch die Ergebnisse mit dem Ledoit-Wolf-Schätzer.

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
