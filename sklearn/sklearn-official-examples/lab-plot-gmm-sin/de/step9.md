# Ergebnisse des Bayesischen GMM mit hohem Konzentrations-Prior plotten

Wir werden die Ergebnisse des Bayesischen Gaussian Mixture Models mit einem Dirichlet-Prozess-Prior und einem hohen Wert für das Konzentrations-Prior plotten.

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
