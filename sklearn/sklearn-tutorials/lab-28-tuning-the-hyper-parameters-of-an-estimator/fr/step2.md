# Chargez le jeu de données

Ensuite, chargeons le jeu de données avec lequel nous allons travailler. Nous pouvons utiliser n'importe quel jeu de données de notre choix pour cet exercice.

```python
from sklearn.datasets import load_iris

# Chargez le jeu de données iris
iris = load_iris()

# Divisez les données en caractéristiques et en cible
X = iris.data
y = iris.target
```
