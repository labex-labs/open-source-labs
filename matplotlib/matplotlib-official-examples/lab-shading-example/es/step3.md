# Crear gráficos de relieve con sombreado

Ahora crearemos los gráficos de relieve con sombreado utilizando la clase `LightSource`. Crearemos dos subgráficos, uno con datos mapeados a un mapa de colores y el otro con intensidad de iluminación.

```python
# Ilumine la escena desde el noroeste
ls = LightSource(azdeg=315, altdeg=45)

fig, axs = plt.subplots(ncols=2, nrows=2)
for ax in axs.flat:
    ax.set(xticks=[], yticks=[])

axs[0, 0].imshow(z, cmap=cmap)
axs[0, 0].set(xlabel='Datos mapeados a un mapa de colores')

axs[0, 1].imshow(ls.hillshade(z, vert_exag=ve), cmap='gray')
axs[0, 1].set(xlabel='Intensidad de iluminación')
```

Crearemos otros dos subgráficos, uno con `blend_mode` establecido en "hsv" y el otro en "overlay".

```python
rgb = ls.shade(z, cmap=cmap, vert_exag=ve, blend_mode='hsv')
axs[1, 0].imshow(rgb)
axs[1, 0].set(xlabel='Modo de mezcla: "hsv" (predeterminado)')

rgb = ls.shade(z, cmap=cmap, vert_exag=ve, blend_mode='overlay')
axs[1, 1].imshow(rgb)
axs[1, 1].set(xlabel='Modo de mezcla: "overlay"')
```
