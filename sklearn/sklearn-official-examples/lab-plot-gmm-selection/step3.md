# Model Training and Selection

We vary the number of components from 1 to 6 and the type of covariance parameters to use:

- `"full"`: each component has its own general covariance matrix.
- `"tied"`: all components share the same general covariance matrix.
- `"diag"`: each component has its own diagonal covariance matrix.
- `"spherical"`: each component has its own single variance.

We score the different models and keep the best model (the lowest BIC). This is done by using `GridSearchCV` and a user-defined score function which returns the negative BIC score. The best set of parameters and estimator are stored in `best_parameters_` and `best_estimator_`, respectively.

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
