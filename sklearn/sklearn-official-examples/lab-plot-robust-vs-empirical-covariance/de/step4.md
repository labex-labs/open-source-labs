# Schätze empirische Kovarianzmatrix

In diesem Schritt schätzen wir eine empirische Kovarianzmatrix des Datensatzes mithilfe des Maximum Likelihood Estimate (MLE)-Schätzers.

```python
# Schätze eine empirische Kovarianzmatrix des Datensatzes
emp_cov = EmpiricalCovariance().fit(X).covariance_
```
