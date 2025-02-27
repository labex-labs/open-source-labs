# Определяем оценщики

В этом шаге мы определяем двух оценщиков. Первый оценщик использует априорное распределение Дирихле для задания количества компонентов с ненулевыми весами. Второй оценщик использует априорный Дирихлева процесс для выбора количества компонентов.

```python
estimators = [
    (
        "Конечная смесь с априорным распределением Дирихле\nи " r"$\gamma_0=$",
        BayesianGaussianMixture(
            weight_concentration_prior_type="dirichlet_distribution",
            n_components=2 * n_components,
            reg_covar=0,
            init_params="random",
            max_iter=1500,
            mean_precision_prior=0.8,
            random_state=random_state,
        ),
        [0.001, 1, 1000],
    ),
    (
        "Бесконечная смесь с априорным Дирихлева процессом\n и" r"$\gamma_0=$",
        BayesianGaussianMixture(
            weight_concentration_prior_type="dirichlet_process",
            n_components=2 * n_components,
            reg_covar=0,
            init_params="random",
            max_iter=1500,
            mean_precision_prior=0.8,
            random_state=random_state,
        ),
        [1, 1000, 100000],
    ),
]
```
