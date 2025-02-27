# Ajustar un modelo mixto gaussiano bayesiano con una distribución a priori de proceso de Dirichlet

Ahora ajustaremos un modelo mixto gaussiano bayesiano con una distribución a priori de proceso de Dirichlet. Estableceremos un valor alto de la concentración a priori para dar al modelo más libertad para modelar la estructura de detalle de los datos.

```python
dpgmm = mixture.BayesianGaussianMixture(
    n_components=10,
    covariance_type="full",
    weight_concentration_prior=1e2,
    weight_concentration_prior_type="dirichlet_process",
    mean_precision_prior=1e-2,
    covariance_prior=1e0 * np.eye(2),
    init_params="kmeans",
    max_iter=100,
    random_state=2,
).fit(X)
```
