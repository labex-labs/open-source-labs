# Sample from Bayesian GMM with High Concentration Prior

We will now sample from the Bayesian Gaussian Mixture Model with a Dirichlet process prior and a high value of the concentration prior.

```python
X_s, y_s = dpgmm.sample(n_samples=2000)
plot_samples(
    X_s,
    y_s,
    dpgmm.n_components,
    1,
    "Gaussian mixture with a Dirichlet process prior "
    r"for $\gamma_0=100$ sampled with $2000$ samples.",
)
```
