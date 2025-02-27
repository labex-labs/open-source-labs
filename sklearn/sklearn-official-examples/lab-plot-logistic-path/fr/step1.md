# Charger l'ensemble de données Iris

Nous allons charger l'ensemble de données Iris à partir de la bibliothèque scikit-learn. L'ensemble de données contient quatre caractéristiques : Longueur du sépale, Largeur du sépale, Longueur des pétales et Largeur des pétales. Nous n'utiliserons que les deux premières caractéristiques pour la classification binaire.

```python
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data
y = iris.target

X = X[y!= 2] # Utiliser seulement les deux premières caractéristiques pour la classification binaire
y = y[y!= 2]

X /= X.max() # Normaliser X pour accélérer la convergence
```
