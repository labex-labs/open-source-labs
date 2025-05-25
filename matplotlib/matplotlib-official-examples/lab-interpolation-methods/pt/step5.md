# Exibir Imagens

Exiba as imagens usando a função `imshow` e diferentes métodos de interpolação.

```python
for ax, interp_method in zip(axs.flat, methods):
    ax.imshow(grid, interpolation=interp_method, cmap='viridis')
    ax.set_title(str(interp_method))
```
