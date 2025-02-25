# Anzeigen von Bildern

Zeigen Sie die Bilder mit der `imshow`-Funktion und verschiedenen Interpolationsmethoden an.

```python
for ax, interp_method in zip(axs.flat, methods):
    ax.imshow(grid, interpolation=interp_method, cmap='viridis')
    ax.set_title(str(interp_method))
```
