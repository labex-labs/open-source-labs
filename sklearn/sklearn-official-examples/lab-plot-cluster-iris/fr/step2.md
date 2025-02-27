# Chargement des données

Ensuite, nous allons charger l'ensemble de données iris, qui est un ensemble de données populaire en apprentissage automatique. Cet ensemble de données contient des informations sur les caractéristiques de différents types de fleurs de lys. Nous allons utiliser cet ensemble de données pour démontrer l'algorithme de regroupement K-Means.

```python
iris = datasets.load_iris()
X = iris.data
y = iris.target
```
