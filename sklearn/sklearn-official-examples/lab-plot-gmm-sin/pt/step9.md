# Plotar os Resultados do Modelo GMM Bayesiano com Prior de Concentração Alta

Plotaremos os resultados do Modelo de Mistura Gaussiana Bayesiano com uma prior de processo Dirichlet e um valor alto para a prior de concentração.

```python
plot_results(
    X,
    dpgmm.predict(X),
    dpgmm.means_,
    dpgmm.covariances_,
    2,
    "Modelos de mistura gaussiana bayesianos com uma prior de processo Dirichlet "
    r"para $\gamma_0=100$",
)
```
