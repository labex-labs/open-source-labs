# Échantillonnage à partir du modèle mixte gaussien bayésien avec une loi a priori de forte concentration

Nous allons maintenant échantillonner à partir du modèle mixte gaussien bayésien avec une loi a priori de processus de Dirichlet et une valeur élevée de la concentration a priori.

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
