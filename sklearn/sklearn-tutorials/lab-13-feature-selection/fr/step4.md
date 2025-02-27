# Sélection de fonctionnalités en utilisant SelectFromModel

La classe `SelectFromModel` est un méta-transformateur qui peut être utilisé avec tout estimateur qui attribue une importance à chaque fonctionnalité. Elle sélectionne les fonctionnalités en fonction de leur importance et élimine les fonctionnalités inférieures à un seuil spécifié.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectFromModel

# Charge le jeu de données Iris
X, y = load_iris(return_X_y=True)

# Initialise RandomForestClassifier comme estimateur
estimateur = RandomForestClassifier()

# Initialise SelectFromModel avec l'estimateur et le seuil "moyenne"
sélecteur = SelectFromModel(estimateur, seuil="moyenne")

# Sélectionne les meilleures fonctionnalités
X_sélectionné = sélecteur.fit_transform(X, y)

print("Forme originale de X :", X.shape)
print("Forme de X avec les fonctionnalités sélectionnées :", X_sélectionné.shape)
print("Fonctionnalités sélectionnées :", sélecteur.get_support(indices=True))
```

Dans cet exemple, nous utilisons un classifieur à forêt aléatoire comme estimateur et sélectionnons les fonctionnalités dont l'importance est supérieure à l'importance moyenne. La sortie montrera la forme originale de l'ensemble de données et la forme après la sélection des meilleures fonctionnalités.
