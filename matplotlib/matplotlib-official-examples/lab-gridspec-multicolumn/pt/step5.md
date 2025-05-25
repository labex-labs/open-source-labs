# Personalizar subplots

Podemos personalizar os subplots conforme necessário. Por exemplo, podemos definir o título da figura usando a função `fig.suptitle()`, e podemos formatar os eixos usando a função `format_axes()`.

```python
fig.suptitle("GridSpec")

def format_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)

format_axes(fig)
```
