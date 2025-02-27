# Sélection de fonctionnalités avec la sélection séquentielle de fonctionnalités

Nous utilisons le Sélecteur séquentiel de fonctionnalités (SFS) pour sélectionner les fonctionnalités. Le SFS est une procédure gourmande où, à chaque itération, nous choisissons la meilleure nouvelle fonctionnalité à ajouter à nos fonctionnalités sélectionnées en fonction d'un score de validation croisée. Nous pouvons également aller dans la direction inverse (SFS arrière), c'est-à-dire commencer avec toutes les fonctionnalités et choisir gourmandement les fonctionnalités à supprimer une par une.

```python
from sklearn.feature_selection import SequentialFeatureSelector

sfs_forward = SequentialFeatureSelector(ridge, n_features_to_select=2, direction="forward").fit(X, y)
sfs_backward = SequentialFeatureSelector(ridge, n_features_to_select=2, direction="backward").fit(X, y)

print(f"Features selected by forward sequential selection: {feature_names[sfs_forward.get_support()]}")
print(f"Features selected by backward sequential selection: {feature_names[sfs_backward.get_support()]}")
```
