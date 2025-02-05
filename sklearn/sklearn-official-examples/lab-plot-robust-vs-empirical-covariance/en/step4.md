# Estimate Empirical Covariance Matrix

In this step, we estimate an empirical covariance matrix of the dataset using the Maximum Likelihood Estimate (MLE) estimator.

```python
# Estimate an empirical covariance matrix of the dataset
emp_cov = EmpiricalCovariance().fit(X).covariance_
```
