# Fit MCD and MLE Covariance Estimators to Data

We will fit the MCD and MLE based covariance estimators to our data and print the estimated covariance matrices. Note that the estimated variance of feature 2 is much higher with the MLE based estimator (7.5) than that of the MCD robust estimator (1.2). This shows that the MCD based robust estimator is much more resistant to the outlier samples, which were designed to have a much larger variance in feature 2.

```python
from sklearn.covariance import EmpiricalCovariance, MinCovDet

# fit a MCD robust estimator to data
robust_cov = MinCovDet().fit(X)
# fit a MLE estimator to data
emp_cov = EmpiricalCovariance().fit(X)
print(
    "Estimated covariance matrix:\nMCD (Robust):\n{}\nMLE:\n{}".format(
        robust_cov.covariance_, emp_cov.covariance_
    )
)
```
