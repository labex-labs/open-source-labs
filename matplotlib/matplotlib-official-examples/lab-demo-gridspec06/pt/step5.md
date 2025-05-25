# Mostrar Apenas os Spines Externos

Nesta etapa, removeremos os spines (bordas) para os subplots internos e mostraremos apenas os spines externos. Isso fará com que o gráfico pareça mais limpo.

```python
for ax in fig.get_axes():
    ss = ax.get_subplotspec()
    ax.spines.top.set_visible(ss.is_first_row())
    ax.spines.bottom.set_visible(ss.is_last_row())
    ax.spines.left.set_visible(ss.is_first_col())
    ax.spines.right.set_visible(ss.is_last_col())
```
