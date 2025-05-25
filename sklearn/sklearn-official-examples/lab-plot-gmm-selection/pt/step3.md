# Treinamento e Seleção do Modelo

Variamos o número de componentes de 1 a 6 e o tipo de parâmetros de covariância a usar:

- `"full"`: cada componente tem sua própria matriz de covariância geral.
- `"tied"`: todos os componentes compartilham a mesma matriz de covariância geral.
- `"diag"`: cada componente tem sua própria matriz de covariância diagonal.
- `"spherical"`: cada componente tem sua própria variância única.

Avalia-se os diferentes modelos e mantém-se o melhor modelo (o menor BIC). Isto é feito usando `GridSearchCV` e uma função de pontuação definida pelo utilizador que retorna a pontuação BIC negativa. O melhor conjunto de parâmetros e o estimador são armazenados em `best_parameters_` e `best_estimator_`, respetivamente.

```python
from sklearn.mixture import GaussianMixture
from sklearn.model_selection import GridSearchCV

def gmm_bic_score(estimator, X):
    """Callable to pass to GridSearchCV that will use the BIC score."""
    # Make it negative since GridSearchCV expects a score to maximize
    return -estimator.bic(X)

param_grid = {
    "n_components": range(1, 7),
    "covariance_type": ["spherical", "tied", "diag", "full"],
}
grid_search = GridSearchCV(
    GaussianMixture(), param_grid=param_grid, scoring=gmm_bic_score
)
grid_search.fit(X)
```
