# Fit a Bayesian Gaussian Mixture Model with a Dirichlet process prior

We will now fit a Bayesian Gaussian Mixture Model with a Dirichlet process prior. We will set a high value of the concentration prior to give the model more liberty to model the fine-grained structure of the data.

```python
dpgmm = mixture.BayesianGaussianMixture(
    n_components=10,
    covariance_type="full",
    weight_concentration_prior=1e2,
    weight_concentration_prior_type="dirichlet_process",
    mean_precision_prior=1e-2,
    covariance_prior=1e0 * np.eye(2),
    init_params="kmeans",
    max_iter=100,
    random_state=2,
).fit(X)
```


