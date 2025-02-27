# Suppression de fonctionnalités avec une faible variance

La classe `VarianceThreshold` dans scikit-learn peut être utilisée pour supprimer les fonctionnalités avec une faible variance. Les fonctionnalités avec une faible variance ne fournissent généralement pas beaucoup d'informations pour le modèle. Nous allons démontrer comment utiliser `VarianceThreshold` pour supprimer les fonctionnalités à variance nulle.

```python
from sklearn.feature_selection import VarianceThreshold

X = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 1, 1]]

# Initialise VarianceThreshold avec un seuil de variabilité de 80%
sel = VarianceThreshold(seuil=(.8 * (1 -.8)))

# Sélectionne les fonctionnalités avec une forte variabilité
X_sélectionné = sel.fit_transform(X)

print("Forme originale de X :", X.shape)
print("Forme de X avec les fonctionnalités sélectionnées :", X_sélectionné.shape)
print("Fonctionnalités sélectionnées :", sel.get_support(indices=True))
```

Ce extrait de code démontre comment utiliser `VarianceThreshold` pour supprimer les fonctionnalités à variance nulle d'un ensemble de données. La sortie montrera la forme originale de l'ensemble de données et la forme après la sélection des fonctionnalités avec une forte variabilité.
