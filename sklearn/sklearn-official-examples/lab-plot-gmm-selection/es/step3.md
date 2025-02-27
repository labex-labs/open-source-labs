# Entrenamiento y selección de modelos

Variamos el número de componentes de 1 a 6 y el tipo de parámetros de covarianza a utilizar:

- `"full"`: cada componente tiene su propia matriz de covarianza general.
- `"tied"`: todos los componentes comparten la misma matriz de covarianza general.
- `"diag"`: cada componente tiene su propia matriz de covarianza diagonal.
- `"spherical"`: cada componente tiene su propia varianza única.

Evaluamos los diferentes modelos y mantenemos el mejor modelo (el BIC más bajo). Esto se hace utilizando `GridSearchCV` y una función de puntuación definida por el usuario que devuelve la puntuación negativa del BIC. El mejor conjunto de parámetros y el estimador se almacenan en `best_parameters_` y `best_estimator_`, respectivamente.

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
