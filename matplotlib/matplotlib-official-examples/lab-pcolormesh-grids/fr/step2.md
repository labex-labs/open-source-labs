# Création de données pour la visualisation

Ensuite, nous allons créer une grille 2D que nous utiliserons pour la visualisation. Nous pouvons créer une grille à l'aide de la fonction `meshgrid` de NumPy. La fonction `meshgrid` crée une grille de points à partir de deux vecteurs, `x` et `y`, qui représentent les coordonnées des points de la grille. Nous allons créer une grille de 5x5 points à l'aide du bloc de code suivant :

```python
nrows = 5
ncols = 5
x = np.arange(ncols + 1)
y = np.arange(nrows + 1)
X, Y = np.meshgrid(x, y)
Z = X + Y
```
