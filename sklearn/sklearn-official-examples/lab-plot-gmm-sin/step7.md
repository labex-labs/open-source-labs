# Sample from Bayesian GMM with Low Concentration Prior

We will now sample from the Bayesian Gaussian Mixture Model with a Dirichlet process prior and a low value of the concentration prior.

```python
X_s, y_s = dpgmm.sample(n_samples=2000)
plot_samples(
    X_s,
    y_s,
    dpgmm.n_components,
    0,
    "Gaussian mixture with a Dirichlet process prior "
    r"for $\gamma_0=0.01$ sampled with $2000$ samples.",
)
```


