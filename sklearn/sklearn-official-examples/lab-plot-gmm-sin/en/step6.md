# Plot the Results of Bayesian GMM with Low Concentration Prior

We will plot the results of the Bayesian Gaussian Mixture Model with a Dirichlet process prior and a low value of the concentration prior.

```python
plot_results(
    X,
    dpgmm.predict(X),
    dpgmm.means_,
    dpgmm.covariances_,
    1,
    "Bayesian Gaussian mixture models with a Dirichlet process prior "
    r"for $\gamma_0=0.01$.",
)
```
