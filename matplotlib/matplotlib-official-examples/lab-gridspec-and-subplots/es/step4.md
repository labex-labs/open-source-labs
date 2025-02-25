# Quitar los ejes subyacentes

Quitamos los ejes subyacentes que están cubiertos por los ejes más grandes que crearemos en el siguiente paso.

```python
for ax in axs[1:, -1]:
    ax.remove()
```
