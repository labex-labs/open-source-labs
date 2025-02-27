# Élimination récursive de fonctionnalités

L'élimination récursive de fonctionnalités (RFE) est une méthode de sélection de fonctionnalités qui considère de manière récursive des ensembles de fonctionnalités de plus en plus petits pour sélectionner les plus importantes. Elle fonctionne en entraînant un estimateur externe avec des poids attribués aux fonctionnalités et en éliminant les fonctionnalités les moins importantes.

```python
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.feature_selection import RFE

# Charge le jeu de données Iris
X, y = load_iris(return_X_y=True)

# Initialise SVC comme estimateur externe
estimateur = SVC(kernel="linear")

# Initialise RFE avec l'estimateur externe et sélectionne 2 fonctionnalités
sélecteur = RFE(estimateur, n_features_to_select=2)

# Sélectionne les meilleures fonctionnalités
X_sélectionné = sélecteur.fit_transform(X, y)

print("Forme originale de X :", X.shape)
print("Forme de X avec les fonctionnalités sélectionnées :", X_sélectionné.shape)
print("Fonctionnalités sélectionnées :", sélecteur.get_support(indices=True))
```

Dans cet exemple, nous utilisons un classifieur à vecteurs de support (SVC) comme estimateur externe et sélectionnons les deux meilleures fonctionnalités à partir du jeu de données Iris. La sortie montrera la forme originale de l'ensemble de données et la forme après la sélection des meilleures fonctionnalités.
