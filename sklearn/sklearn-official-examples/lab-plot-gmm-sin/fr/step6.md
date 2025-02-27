# Tracer les résultats du modèle mixte gaussien bayésien avec une loi a priori de faible concentration

Nous allons tracer les résultats du modèle mixte gaussien bayésien avec une loi a priori de processus de Dirichlet et une valeur faible de la concentration a priori.

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
