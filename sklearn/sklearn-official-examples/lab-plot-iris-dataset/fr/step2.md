# Charger le Jeu de données Iris

Nous allons charger le Jeu de données Iris à l'aide de la fonction intégrée `load_iris` de Scikit-learn.

```python
iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features.
y = iris.target
```
