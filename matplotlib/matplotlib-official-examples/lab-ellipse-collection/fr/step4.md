# Définir la couleur des ellipses

Nous définissons la couleur de chaque ellipse dans la `EllipseCollection` en fonction de la somme de ses coordonnées x et y.

```python
ec.set_array((X + Y).ravel())
```
