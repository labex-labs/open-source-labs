# Ajustar um Modelo de Mistura Gaussiana Bayesiano com uma Prior de Processo Dirichlet

Agora, ajustaremos um Modelo de Mistura Gaussiana Bayesiano com uma prior de processo Dirichlet. Definiremos um valor alto para a prior de concentração para dar ao modelo mais liberdade para modelar a estrutura detalhada dos dados.

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
