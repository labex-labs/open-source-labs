# Définissez les lignes de niveau et les polygones

L'étape suivante est de définir les lignes de niveau et les polygones. Dans cet exemple, nous avons des lignes et des contours remplis entre deux niveaux.

```python
# Les lignes de niveau pour chaque niveau sont une liste/tuple de polygones.
lines0 = [[[0, 0], [0, 4]]]
lines1 = [[[2, 0], [1, 2], [1, 3]]]
lines2 = [[[3, 0], [3, 2]], [[3, 3], [3, 4]]]  # Notez deux lignes.

# Les contours remplis entre deux niveaux sont également une liste/tuple de polygones.
# Les points peuvent être ordonnés dans le sens horaire ou antihoraire.
filled01 = [[[0, 0], [0, 4], [1, 3], [1, 2], [2, 0]]]
filled12 = [[[2, 0], [3, 0], [3, 2], [1, 3], [1, 2]],   # Notez deux polygones.
            [[1, 4], [3, 4], [3, 3]]]
```
