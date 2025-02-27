# Effectuez une recherche en grille avec validation croisée

La recherche en grille explore de manière exhaustive toutes les combinaisons possibles d'hyperparamètres dans la grille de paramètres spécifiée. Elle évalue les performances de chaque combinaison en utilisant la validation croisée.

```python
# Créez une instance de GridSearchCV
grid_search = GridSearchCV(svc, param_grid, cv=5)

# Ajustez les données pour effectuer la recherche en grille
grid_search.fit(X, y)

# Affichez la meilleure combinaison d'hyperparamètres
print('Meilleurs hyperparamètres :', grid_search.best_params_)
```
