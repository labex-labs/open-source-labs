# Amostrar do Modelo GMM Bayesiano com Prior de Concentração Baixa

Agora, amostraremos do Modelo de Mistura Gaussiana Bayesiano com uma prior de processo Dirichlet e um valor baixo para a prior de concentração.

```python
X_s, y_s = dpgmm.sample(n_samples=2000)
plot_samples(
    X_s,
    y_s,
    dpgmm.n_components,
    0,
    "Mistura gaussiana com uma prior de processo Dirichlet "
    r"para $\gamma_0=0.01$ amostrada com $2000$ amostras.",
)
```
