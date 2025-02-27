# Entraînement et sélection du modèle

Nous faisons varier le nombre de composants de 1 à 6 et le type de paramètres de covariance à utiliser :

- `"full"` : chaque composant a sa propre matrice de covariance générale.
- `"tied"` : tous les composants partagent la même matrice de covariance générale.
- `"diag"` : chaque composant a sa propre matrice de covariance diagonale.
- `"spherical"` : chaque composant a sa propre variance unique.

Nous évaluons les différents modèles et conservons le meilleur modèle (celui avec le BIC le plus bas). Cela est fait en utilisant `GridSearchCV` et une fonction de score définie par l'utilisateur qui renvoie le score BIC négatif. Le meilleur ensemble de paramètres et l'estimateur sont stockés respectivement dans `best_parameters_` et `best_estimator_`.

```python
from sklearn.mixture import GaussianMixture
from sklearn.model_selection import GridSearchCV

def gmm_bic_score(estimator, X):
    """Callable à passer à GridSearchCV qui utilisera le score BIC."""
    # Rendre négatif car GridSearchCV attend un score à maximiser
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
