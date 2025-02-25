# Chargez les données d'image

Nous allons utiliser un exemple de données d'image appelées `bivariate_normal.npy` provenant de `cbook` pour démontrer l'ImageGrid. Nous chargeons les données d'image à l'aide de la fonction `get_sample_data` de `cbook`.

```python
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")
im1 = Z
im2 = Z[:, :10]
im3 = Z[:, 10:]
vmin, vmax = Z.min(), Z.max()
```
