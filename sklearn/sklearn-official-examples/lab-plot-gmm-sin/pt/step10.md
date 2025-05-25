# Amostrar do Modelo GMM Bayesiano com Prior de Concentração Alta

Agora, amostraremos do Modelo de Mistura Gaussiana Bayesiano com uma prior de processo Dirichlet e um valor alto para a prior de concentração.

```python
X_s, y_s = dpgmm.sample(n_samples=2000)
plot_samples(
    X_s,
    y_s,
    dpgmm.n_components,
    1,
    "Mistura gaussiana com uma prior de processo Dirichlet "
    r"para $\gamma_0=100$ amostrada com $2000$ amostras.",
)
```
