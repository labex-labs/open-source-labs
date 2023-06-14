# Fit a Bayesian Gaussian Mixture Model with a Dirichlet process prior

We will now fit a Bayesian Gaussian Mixture Model with a Dirichlet process prior. We will set a low value of the concentration prior to make the model favor a lower number of active components.

```python
dpgmm = mixture.BayesianGaussianMixture(
    n_components=10,
    covariance_type="full",
    weight_concentration_prior=1e-2,
    weight_concentration_prior_type="dirichlet_process",
    mean_precision_prior=1e-2,
    covariance_prior=1e0 * np.eye(2),
    init_params="random",
    max_iter=100,
    random_state=2,
).fit(X)
```


