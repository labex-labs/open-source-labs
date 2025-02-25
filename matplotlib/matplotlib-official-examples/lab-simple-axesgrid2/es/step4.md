# Mostrar imágenes en el ImageGrid

Finalmente, mostramos las imágenes en el ImageGrid usando la función `imshow` y la función `zip` para iterar a través de los ejes en la cuadrícula.

```python
for ax, im in zip(grid, [im1, im2, im3]):
    ax.imshow(im, origin="lower", vmin=vmin, vmax=vmax)

plt.show()
```
