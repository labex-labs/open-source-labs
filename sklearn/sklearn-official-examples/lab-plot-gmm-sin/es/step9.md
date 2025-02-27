# Graficar los resultados del modelo mixto gaussiano bayesiano con una distribución a priori de alta concentración

Graficaremos los resultados del modelo mixto gaussiano bayesiano con una distribución a priori de proceso de Dirichlet y un valor alto de la concentración a priori.

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
