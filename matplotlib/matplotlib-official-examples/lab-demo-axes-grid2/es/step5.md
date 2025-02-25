# Demostración 2 - Barra de color compartida

Crearemos una cuadrícula de 3 imágenes con una barra de color compartida con el siguiente código:

```python
grid2 = ImageGrid(
    fig, 212, nrows_ncols=(1, 3), axes_pad=0.05, label_mode="1", share_all=True,
    cbar_location="right", cbar_mode="single", cbar_size="10%", cbar_pad=0.05)
grid2[0].set(xlabel="X", ylabel="Y", xticks=[-2, 0], yticks=[-2, 0, 2])

clim = (np.min(ZS), np.max(ZS))
for ax, z in zip(grid2, ZS):
    im = ax.imshow(z, clim=clim, origin="lower", extent=extent)

# Con cbar_mode="single", el atributo cax de todos los ejes es idéntico.
ax.cax.colorbar(im)

for ax, im_title in zip(grid2, ["(a)", "(b)", "(c)"]):
    add_inner_title(ax, im_title, loc='upper left')
```

- Creamos una cuadrícula de 3 imágenes usando `ImageGrid`.
- Establecemos el `cbar_mode` en "single" para agregar una barra de color compartida.
- Establecemos el parámetro `share_all` en True para compartir los ejes x e y en todas las imágenes.
- Establecemos el parámetro `cbar_location` en "right" para posicionar la barra de color a la derecha.
- Establecemos los `xticks` y `yticks` para la primera imagen.
- Recorremos cada imagen y agregamos la imagen al eje usando `imshow`.
- Establecemos el parámetro `clim` para asegurarnos de que todas las imágenes usen la misma escala de colores.
- Agregamos una barra de color compartida al eje usando `ax.cax.colorbar`.
- Agregamos un título a cada imagen usando `add_inner_title`.
