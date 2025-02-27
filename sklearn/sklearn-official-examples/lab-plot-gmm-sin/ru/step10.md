# Выборка из смеси Гауссовых распределений с априорным распределением Дирихле и высоким значением априорной концентрации

Теперь мы будем получать выборку из смеси Гауссовых распределений с априорным распределением Дирихле и высоким значением априорной концентрации.

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
