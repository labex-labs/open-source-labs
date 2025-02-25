# Crear las rejillas de imágenes

Crearemos dos rejillas de imágenes para mostrar nuestras imágenes. La primera rejilla de imágenes tendrá dos filas y dos columnas, y la segunda rejilla de imágenes también tendrá dos filas y dos columnas.

```python
grid1 = ImageGrid(fig, 121, (2, 2), axes_pad=0.1, aspect=True, share_all=True)
grid2 = ImageGrid(fig, 122, (2, 2), axes_pad=0.1, aspect=True, share_all=True)
```
