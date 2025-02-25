# Création des données

Nous allons créer les données pour notre graphique de champ de flux à l'aide de la bibliothèque Numpy. Dans cet exemple, nous allons créer une grille de maillage avec 100 points dans les deux directions et calculer les composantes U et V de notre champ vectoriel.

```python
w = 3
Y, X = np.mgrid[-w:w:100j, -w:w:100j]
U = -1 - X**2 + Y
V = 1 + X - Y**2
speed = np.sqrt(U**2 + V**2)
```
