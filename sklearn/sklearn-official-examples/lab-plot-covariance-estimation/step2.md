# Compute the Likelihood on Test Data

We calculate the negative log-likelihood on the test data using the `ShrunkCovariance` class from the `sklearn.covariance` module and the `log_likelihood` function from the `scipy.linalg` module. We span a range of possible shrinkage coefficient values and compute the likelihood for each value.

```python
from sklearn.covariance import ShrunkCovariance, empirical_covariance, log_likelihood
from scipy import linalg

shrinkages = np.logspace(-2, 0, 30)
negative_logliks = [
    -ShrunkCovariance(shrinkage=s).fit(X_train).score(X_test) for s in shrinkages
]

real_cov = np.dot(coloring_matrix.T, coloring_matrix)
emp_cov = empirical_covariance(X_train)
loglik_real = -log_likelihood(emp_cov, linalg.inv(real_cov))
```


