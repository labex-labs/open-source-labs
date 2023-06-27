# Fit a Gaussian Mixture Model with EM

We will fit a classical Gaussian Mixture Model with 10 components fit with the Expectation-Maximization algorithm.

```python
# Fit a Gaussian mixture with EM using ten components
gmm = mixture.GaussianMixture(
    n_components=10, covariance_type="full", max_iter=100
).fit(X)
```
