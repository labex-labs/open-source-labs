# Definir estimadores

En este paso, definimos dos estimadores. El primer estimador utiliza una prioridad de distribución de Dirichlet para establecer el número de componentes con pesos no nulos. El segundo estimador utiliza una prioridad de proceso de Dirichlet para seleccionar el número de componentes.

```python
estimators = [
    (
        "Mezcla finita con una distribución de Dirichlet\nprior y " r"$\gamma_0=$",
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
        "Mezcla infinita con un proceso de Dirichlet\n prior y" r"$\gamma_0=$",
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
