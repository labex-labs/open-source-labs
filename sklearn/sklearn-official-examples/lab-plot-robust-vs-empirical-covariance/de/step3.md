# Schätze robuste Kovarianzmatrix

In diesem Schritt schätzen wir eine robuste Kovarianzmatrix des Datensatzes mithilfe des Minimum Covariance Determinant (MCD)-Schätzers.

```python
# Schätze eine robuste Kovarianzmatrix des Datensatzes
mcd = MinCovDet().fit(X)
robust_cov = mcd.covariance_
```
