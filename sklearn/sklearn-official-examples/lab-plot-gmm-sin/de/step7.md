# Aus dem Bayesischen GMM mit niedrigem Konzentrations-Prior abprobieren

Wir werden nun aus dem Bayesischen Gaussian Mixture Model mit einem Dirichlet-Prozess-Prior und einem niedrigen Wert für das Konzentrations-Prior abprobieren.

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
