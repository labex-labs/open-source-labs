# Estimate Robust Covariance Matrix

In this step, we estimate a robust covariance matrix of the dataset using the Minimum Covariance Determinant (MCD) estimator.

```python
# Estimate a robust covariance matrix of the dataset
mcd = MinCovDet().fit(X)
robust_cov = mcd.covariance_
```
