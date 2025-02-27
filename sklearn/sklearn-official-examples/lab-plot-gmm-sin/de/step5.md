# Ein Bayesisches Gaussian Mixture Model mit einem Dirichlet-Prozess-Prior anpassen

Wir werden nun ein Bayesisches Gaussian Mixture Model mit einem Dirichlet-Prozess-Prior anpassen. Wir werden einen niedrigen Wert für das Konzentrations-Prior setzen, um das Modell dazu zu veranlassen, eine kleinere Anzahl aktiver Komponenten zu bevorzugen.

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
