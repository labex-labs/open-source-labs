# Tomar muestras del modelo mixto gaussiano bayesiano con una distribución a priori de alta concentración

Ahora tomaremos muestras del modelo mixto gaussiano bayesiano con una distribución a priori de proceso de Dirichlet y un valor alto de la concentración a priori.

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
