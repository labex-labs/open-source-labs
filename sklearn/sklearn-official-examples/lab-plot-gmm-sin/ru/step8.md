# Подгонка смеси Гауссовых распределений с априорным распределением Дирихле

Теперь мы подгоним смесь Гауссовых распределений с априорным распределением Дирихле. Мы установим высокое значение априорной концентрации, чтобы дать модели больше свободы для моделирования мелкозернистой структуры данных.

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
