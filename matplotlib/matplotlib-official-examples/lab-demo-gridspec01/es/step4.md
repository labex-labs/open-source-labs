# Anotar los ejes

Para anotar los ejes, podemos recorrer los ejes de la figura y agregar texto usando la función `text` y la función `tick_params` para eliminar las etiquetas de los ticks.

```python
def annotate_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)
```
