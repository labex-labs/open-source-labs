# Построение результатов смеси Гауссовых распределений с априорным распределением Дирихле и высоким значением априорной концентрации

Мы построим результаты смеси Гауссовых распределений с априорным распределением Дирихле и высоким значением априорной концентрации.

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
