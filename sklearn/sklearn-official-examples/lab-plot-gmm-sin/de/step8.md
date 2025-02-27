# Ein Bayesisches Gaussian Mixture Model mit einem Dirichlet-Prozess-Prior anpassen

Wir werden nun ein Bayesisches Gaussian Mixture Model mit einem Dirichlet-Prozess-Prior anpassen. Wir werden einen hohen Wert für das Konzentrations-Prior setzen, um dem Modell mehr Freiheit zu geben, um die feingranulare Struktur der Daten zu modellieren.

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
