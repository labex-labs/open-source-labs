# Definir o estilo do eixo

Finalmente, definiremos o estilo para o eixo x, especificando os rótulos e limites dos ticks (marcas). Definiremos uma função auxiliar `set_axis_style` para realizar isso.

```python
# set style for the axes
labels = ['A', 'B', 'C', 'D']
set_axis_style(ax2, labels)

def set_axis_style(ax, labels):
    ax.set_xticks(np.arange(1, len(labels) + 1))
    ax.set_xticklabels(labels)
    ax.set_xlim(0.25, len(labels) + 0.75)
    ax.set_xlabel('Sample Name')
```
