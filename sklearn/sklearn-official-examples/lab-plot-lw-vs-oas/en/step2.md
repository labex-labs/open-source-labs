# Generate Data

Next, we will generate Gaussian distributed data with a covariance matrix that follows an AR(1) process. We will use `toeplitz` and `cholesky` functions from `scipy.linalg` to generate the covariance matrix.

```python
np.random.seed(0)

n_features = 100
r = 0.1
real_cov = toeplitz(r ** np.arange(n_features))
coloring_matrix = cholesky(real_cov)
```
