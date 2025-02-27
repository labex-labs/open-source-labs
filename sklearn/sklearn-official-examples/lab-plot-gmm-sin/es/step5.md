# Ajustar un modelo mixto gaussiano bayesiano con una distribución a priori de proceso de Dirichlet

Ahora ajustaremos un modelo mixto gaussiano bayesiano con una distribución a priori de proceso de Dirichlet. Estableceremos un valor bajo de la concentración a priori para que el modelo favorezca un número menor de componentes activos.

```python
dpgmm = mixture.BayesianGaussianMixture(
    n_components=10,
    covariance_type="full",
    weight_concentration_prior=1e-2,
    weight_concentration_prior_type="dirichlet_process",
    mean_precision_prior=1e-2,
    covariance_prior=1e0 * np.eye(2),
    init_params="random",
    max_iter=100,
    random_state=2,
).fit(X)
```
