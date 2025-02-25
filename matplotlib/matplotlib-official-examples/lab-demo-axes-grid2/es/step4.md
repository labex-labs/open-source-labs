# Demostración 1 - Barra de color en cada eje

Crearemos una cuadrícula de 3 imágenes con una barra de color en cada eje con el siguiente código:

```python
grid = ImageGrid(
    fig, 211, nrows_ncols=(1, 3), axes_pad=0.05, label_mode="1", share_all=True,
    cbar_location="top", cbar_mode="each", cbar_size="7%", cbar_pad="1%")
grid[0].set(xticks=[-2, 0], yticks=[-2, 0, 2])

for i, (ax, z) in enumerate(zip(grid, ZS)):
    im = ax.imshow(z, origin="lower", extent=extent)
    cb = ax.cax.colorbar(im)
    # Cambiando las marcas de la barra de color
    if i in [1, 2]:
        cb.set_ticks([-1, 0, 1])

for ax, im_title in zip(grid, ["Imagen 1", "Imagen 2", "Imagen 3"]):
    add_inner_title(ax, im_title, loc='lower left')
```

- Creamos una cuadrícula de 3 imágenes usando `ImageGrid`.
- Establecemos el `cbar_mode` en "each" para agregar una barra de color en cada eje.
- Establecemos el parámetro `share_all` en True para compartir los ejes x e y en todas las imágenes.
- Establecemos el parámetro `cbar_location` en "top" para posicionar las barras de color en la parte superior.
- Establecemos los `xticks` y `yticks` para la primera imagen.
- Recorremos cada imagen y agregamos la imagen al eje usando `imshow`.
- Agregamos una barra de color a cada eje usando `ax.cax.colorbar`.
- Establecemos las marcas de la barra de color para la segunda y tercera imágenes.
- Agregamos un título a cada imagen usando `add_inner_title`.
