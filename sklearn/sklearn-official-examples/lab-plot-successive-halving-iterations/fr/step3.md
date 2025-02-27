# Définition de l'espace de paramètres

Définissez un dictionnaire `param_dist` qui contient les hyperparamètres et leurs valeurs respectives à explorer. Les hyperparamètres sont `max_depth`, `max_features`, `min_samples_split`, `bootstrap` et `criterion`. La plage de recherche pour `max_features` et `min_samples_split` est définie à l'aide de la fonction `randint` du module `scipy.stats`. Le code pour définir l'espace de paramètres est le suivant :

```python
param_dist = {
    "max_depth": [3, None],
    "max_features": randint(1, 6),
    "min_samples_split": randint(2, 11),
    "bootstrap": [True, False],
    "criterion": ["gini", "entropy"],
}
```
