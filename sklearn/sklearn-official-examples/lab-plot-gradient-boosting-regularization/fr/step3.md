# Définir les paramètres

Nous allons définir les paramètres pour notre classifieur Gradient Boosting. Nous utiliserons les paramètres suivants :

- n_estimators : nombre d'étapes de boosting à effectuer
- max_leaf_nodes : nombre maximum de nœuds terminaux dans chaque arbre
- max_depth : profondeur maximale de l'arbre
- random_state : graine aléatoire pour la cohérence
- min_samples_split : nombre minimum d'échantillons requis pour diviser un nœud interne

```python
original_params = {
    "n_estimators": 400,
    "max_leaf_nodes": 4,
    "max_depth": None,
    "random_state": 2,
    "min_samples_split": 5,
}
```
