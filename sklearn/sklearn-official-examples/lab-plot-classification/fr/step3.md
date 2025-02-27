# Préparer les données

Nous ne prendrons que les deux premières caractéristiques de l'ensemble de données Iris, qui sont la longueur du sépale et la largeur du sépale. Nous diviserons ensuite les données en matrice de caractéristiques `X` et vecteur cible `y`.

```python
X = iris.data[:, :2]
y = iris.target
```
