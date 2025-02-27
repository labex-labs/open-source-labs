# Effectuez une recherche aléatoire avec validation croisée

La recherche aléatoire prend aléatoirement un sous-ensemble de la grille de paramètres et évalue les performances de chaque combinaison en utilisant la validation croisée. Elle est utile lorsque l'espace de paramètres est grand et qu'il n'est pas possible d'effectuer une recherche exhaustive.

```python
# Créez une instance de RandomizedSearchCV
random_search = RandomizedSearchCV(svc, param_grid, cv=5, n_iter=10, random_state=0)

# Ajustez les données pour effectuer la recherche aléatoire
random_search.fit(X, y)

# Affichez la meilleure combinaison d'hyperparamètres
print('Meilleurs hyperparamètres :', random_search.best_params_)
```
