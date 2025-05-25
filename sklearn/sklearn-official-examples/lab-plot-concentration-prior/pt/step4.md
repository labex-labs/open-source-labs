# Definir Estimadores

Neste passo, definimos dois estimadores. O primeiro estimador utiliza uma distribuição Dirichlet como prior para definir o número de componentes com pesos não nulos. O segundo estimador utiliza uma prior de processo Dirichlet para selecionar o número de componentes.

```python
estimators = [
    (
        "Mistura finita com uma distribuição Dirichlet\nprior e " r"$\gamma_0=$",
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
        "Mistura infinita com uma prior de processo Dirichlet e" r"$\gamma_0=$",
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
