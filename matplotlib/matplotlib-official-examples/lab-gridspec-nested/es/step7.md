# Formatear los ejes

Vamos a formatear los ejes de todos los subgráficos utilizando la función `format_axes`. Esta función agregará una etiqueta de texto a cada subgráfico y eliminará las etiquetas de los ticks.

```python
def format_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)

format_axes(fig)
```
