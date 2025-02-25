# Personalizar subgráficos

Podemos personalizar los subgráficos según sea necesario. Por ejemplo, podemos establecer el título de la figura utilizando la función `fig.suptitle()`, y podemos formatear los ejes utilizando la función `format_axes()`.

```python
fig.suptitle("GridSpec")

def format_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)

format_axes(fig)
```
