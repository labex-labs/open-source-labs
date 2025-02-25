# Création de données pour les ellipses

Nous créons les données pour nos ellipses sous forme de tableaux de coordonnées x, de coordonnées y, de largeur, de hauteur et d'angle.

```python
x = np.arange(10)
y = np.arange(15)
X, Y = np.meshgrid(x, y)

XY = np.column_stack((X.ravel(), Y.ravel()))

ww = X / 10.0
hh = Y / 15.0
aa = X * 9
```
