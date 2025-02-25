# Configurar la figura

Configura la figura utilizando `plt.figure()` y `add_gridspec()`. La figura tendrá una cuadrícula de 2 columnas y n filas, donde n es el número de estilos de flecha. Cada celda de la cuadrícula contendrá un estilo de flecha y sus parámetros predeterminados.

```python
ncol = 2
nrow = (len(styles) + 1) // ncol
axs = (plt.figure(figsize=(4 * ncol, 1 + nrow))
     .add_gridspec(1 + nrow, ncol,
                    wspace=.7, left=.1, right=.9, bottom=0, top=1).subplots())
for ax in axs.flat:
    ax.set_axis_off()
for ax in axs[0, :]:
    ax.text(0,.5, "arrowstyle",
            transform=ax.transAxes, size="large", color="tab:blue",
            horizontalalignment="center", verticalalignment="center")
    ax.text(.35,.5, "default parameters",
            transform=ax.transAxes,
            horizontalalignment="left", verticalalignment="center")
```
