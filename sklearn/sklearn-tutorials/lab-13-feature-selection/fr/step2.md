# Sélection de fonctionnalités univariées

La sélection de fonctionnalités univariées fonctionne en sélectionnant les meilleures fonctionnalités sur la base de tests statistiques univariés. Dans scikit-learn, plusieurs classes implémentent la sélection de fonctionnalités univariées :

- `SelectKBest` : sélectionne les k meilleures fonctionnalités ayant les scores les plus élevés
- `SelectPercentile` : sélectionne un pourcentage spécifié par l'utilisateur des fonctionnalités ayant les scores les plus élevés
- `SelectFpr` : sélectionne les fonctionnalités sur la base du taux de faux positifs
- `SelectFdr` : sélectionne les fonctionnalités sur la base du taux de découverte de faux positifs
- `SelectFwe` : sélectionne les fonctionnalités sur la base de l'erreur globale familiale
- `GenericUnivariateSelect` : permet la sélection avec une stratégie configurable

Voici un exemple d'utilisation de `SelectKBest` pour sélectionner les deux meilleures fonctionnalités à partir du jeu de données Iris :

```python
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif

# Charge le jeu de données Iris
X, y = load_iris(return_X_y=True)

# Initialise SelectKBest avec la fonction de scoring f_classif et k = 2
sélecteur = SelectKBest(f_classif, k = 2)

# Sélectionne les meilleures fonctionnalités
X_sélectionné = sélecteur.fit_transform(X, y)

print("Forme originale de X :", X.shape)
print("Forme de X avec les fonctionnalités sélectionnées :", X_sélectionné.shape)
print("Fonctionnalités sélectionnées :", sélecteur.get_support(indices=True))
```

Dans cet exemple, nous utilisons la fonction de scoring `f_classif` et sélectionnons les deux meilleures fonctionnalités à partir du jeu de données Iris. La sortie montrera la forme originale de l'ensemble de données et la forme après la sélection des meilleures fonctionnalités.
