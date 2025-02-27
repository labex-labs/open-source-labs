# Recherche en grille pour l'optimisation d'hyperparamètres

Nous utiliserons la recherche en grille pour explorer l'espace d'hyperparamètres et trouver les meilleurs hyperparamètres pour notre modèle SVM.

```python
# spécifiez les paramètres à rechercher
param_grid = {
    "average": [True, False],
    "l1_ratio": np.linspace(0, 1, num=10),
    "alpha": np.power(10, np.arange(-2, 1, dtype=float)),
}

# exécutez la recherche en grille
grid_search = GridSearchCV(clf, param_grid=param_grid)

start = time()
grid_search.fit(X, y)

print(
    "GridSearchCV a pris %.2f secondes pour %d paramètres candidats."
    % (time() - start, len(grid_search.cv_results_["params"]))
)

# affichez les résultats
report(grid_search.cv_results_)
```
