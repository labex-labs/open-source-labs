# Aus dem Bayesischen GMM mit hohem Konzentrations-Prior abprobieren

Wir werden nun aus dem Bayesischen Gaussian Mixture Model mit einem Dirichlet-Prozess-Prior und einem hohen Wert für das Konzentrations-Prior abprobieren.

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
