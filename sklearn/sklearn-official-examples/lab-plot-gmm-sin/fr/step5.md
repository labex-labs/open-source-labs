# Ajuster un modèle mixte gaussien bayésien avec une loi a priori de processus de Dirichlet

Nous allons maintenant ajuster un modèle mixte gaussien bayésien avec une loi a priori de processus de Dirichlet. Nous allons définir une valeur faible pour la concentration a priori pour que le modèle privilégie un nombre plus faible de composants actifs.

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
