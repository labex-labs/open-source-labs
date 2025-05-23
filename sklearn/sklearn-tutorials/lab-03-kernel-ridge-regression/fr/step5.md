# Optimiser les hyperparamètres

Dans l'étape précédente, nous avons utilisé les valeurs par défaut des hyperparamètres pour alpha et gamma. Pour améliorer les performances du modèle, nous pouvons optimiser ces hyperparamètres en utilisant la recherche en grille.

```python
from sklearn.model_selection import GridSearchCV

# Define the parameter grid
param_grid = {'alpha': [1e-3, 1e-2, 1e-1, 1, 10],
              'gamma': [1e-3, 1e-2, 1e-1, 1, 10]}

# Perform grid search
grid_search = GridSearchCV(krr, param_grid, cv=5)
grid_search.fit(X, y)

# Get the best hyperparameters
best_alpha = grid_search.best_params_['alpha']
best_gamma = grid_search.best_params_['gamma']
best_krr = grid_search.best_estimator_

print("Best alpha:", best_alpha)
print("Best gamma:", best_gamma)
```
