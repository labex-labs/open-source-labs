# Préparer la grille de données

Nous allons configurer la grille de données pour le tracé de courbes de niveau. Nous utiliserons la fonction `construct_grids` pour y parvenir.

```python
X, Y = np.meshgrid(xgrid[::5], ygrid[::5][::-1])
land_reference = data.coverages[6][::5, ::5]
land_mask = (land_reference > -9999).ravel()

xy = np.vstack([Y.ravel(), X.ravel()]).T
xy = xy[land_mask]
xy *= np.pi / 180.0
```
