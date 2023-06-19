# Plot the Results of Bayesian GMM with High Concentration Prior

We will plot the results of the Bayesian Gaussian Mixture Model with a Dirichlet process prior and a high value of the concentration prior.

```python
plot_results(
    X,
    dpgmm.predict(X),
    dpgmm.means_,
    dpgmm.covariances_,
    2,
    "Bayesian Gaussian mixture models with a Dirichlet process prior "
    r"for $\gamma_0=100$",
)
```


