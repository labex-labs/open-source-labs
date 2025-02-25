# Establecer los límites y etiquetas de la gráfica

Estableceremos los límites y etiquetas de la gráfica para que coincidan con la salida deseada.

```python
for ax in axs:
    ax.set(xlim=(-0.1, 1.1), ylim=(-.8, 3.9), xticks=[], yticks=[])
    ax.set_title(f"usetex={ax.usetex}\n")
```
