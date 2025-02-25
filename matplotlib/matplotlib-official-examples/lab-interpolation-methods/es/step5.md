# Mostrar imágenes

Muestra las imágenes utilizando la función `imshow` y diferentes métodos de interpolación.

```python
for ax, interp_method in zip(axs.flat, methods):
    ax.imshow(grid, interpolation=interp_method, cmap='viridis')
    ax.set_title(str(interp_method))
```
