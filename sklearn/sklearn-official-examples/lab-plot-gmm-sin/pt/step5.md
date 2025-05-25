# Ajustar um Modelo de Mistura Gaussiana Bayesiano com uma Prior de Processo Dirichlet

Agora, ajustaremos um Modelo de Mistura Gaussiana Bayesiano com uma prior de processo Dirichlet. Definiremos um valor baixo para a prior de concentração para fazer com que o modelo favoreça um número menor de componentes ativos.

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
