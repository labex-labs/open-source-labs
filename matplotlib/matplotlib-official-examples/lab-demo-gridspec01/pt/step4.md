# Anotar Eixos

Para anotar os eixos, podemos iterar pelos eixos da figura e adicionar texto usando a função `text` e a função `tick_params` para remover os rótulos das marcas de escala (tick labels).

```python
def annotate_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)
```
