# Tomar muestras del modelo mixto gaussiano bayesiano con una distribución a priori de baja concentración

Ahora tomaremos muestras del modelo mixto gaussiano bayesiano con una distribución a priori de proceso de Dirichlet y un valor bajo de la concentración a priori.

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
