# Modelltraining und -auswahl

Wir variieren die Anzahl der Komponenten von 1 bis 6 und den Typ der Kovarianzparameter, die verwendet werden sollen:

- `"full"`: jede Komponente hat ihre eigene allgemeine Kovarianzmatrix.
- `"tied"`: alle Komponenten teilen die gleiche allgemeine Kovarianzmatrix.
- `"diag"`: jede Komponente hat ihre eigene diagonale Kovarianzmatrix.
- `"spherical"`: jede Komponente hat ihre eigene einfache Varianz.

Wir bewerten die verschiedenen Modelle und behalten das beste Modell (den niedrigsten BIC) bei. Dies wird durch die Verwendung von `GridSearchCV` und einer benutzerdefinierten Score-Funktion erreicht, die den negativen BIC-Wert zurückgibt. Der beste Parameterensatz und der Schätzer werden jeweils in `best_parameters_` und `best_estimator_` gespeichert.

```python
from sklearn.mixture import GaussianMixture
from sklearn.model_selection import GridSearchCV

def gmm_bic_score(estimator, X):
    """Aufrufbar, um an GridSearchCV zu übergeben, der den BIC-Wert verwenden wird."""
    # Machen Sie es negativ, da GridSearchCV erwartet, dass ein Score maximiert wird
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
