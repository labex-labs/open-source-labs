# Creando el trazado

En este paso, crearemos el diagrama de contorno con máscara utilizando la función `contourf()`. Le pasamos las matrices `x`, `y` y `z` a esta función, junto con el argumento `corner_mask` establecido en `True` o `False` según el tipo de trazado que queramos crear.

```python
corner_masks = [False, True]
fig, axs = plt.subplots(ncols=2)
for ax, corner_mask in zip(axs, corner_masks):
    cs = ax.contourf(x, y, z, corner_mask=corner_mask)
    ax.contour(cs, colors='k')
    ax.set_title(f'{corner_mask=}')

    # Plot grid.
    ax.grid(c='k', ls='-', alpha=0.3)

    # Indicate masked points with red circles.
    ax.plot(np.ma.array(x, mask=~mask), y, 'ro')

plt.show()
```
