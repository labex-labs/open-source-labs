# Afficher les images

Affichez les images à l'aide de la fonction `imshow` et de différentes méthodes d'interpolation.

```python
for ax, interp_method in zip(axs.flat, methods):
    ax.imshow(grid, interpolation=interp_method, cmap='viridis')
    ax.set_title(str(interp_method))
```
