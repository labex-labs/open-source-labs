# Formatar os Eixos

Formataremos os eixos de todos os subplots usando a função `format_axes`. Esta função adicionará um rótulo de texto a cada subplot e removerá os rótulos de marcação (tick labels).

```python
def format_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)

format_axes(fig)
```
