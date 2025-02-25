# Cargar los datos de la imagen

Usaremos un ejemplo de datos de imagen llamado `bivariate_normal.npy` de `cbook` para demostrar el ImageGrid. Cargamos los datos de la imagen usando la función `get_sample_data` de `cbook`.

```python
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")
im1 = Z
im2 = Z[:, :10]
im3 = Z[:, 10:]
vmin, vmax = Z.min(), Z.max()
```
