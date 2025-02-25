# Mostrar solo las espinas externas

En este paso, eliminaremos las espinas de las subtramas internas y mostraremos solo las espinas externas. Esto hará que la gráfica se vea más limpia.

```python
for ax in fig.get_axes():
    ss = ax.get_subplotspec()
    ax.spines.top.set_visible(ss.is_first_row())
    ax.spines.bottom.set_visible(ss.is_last_row())
    ax.spines.left.set_visible(ss.is_first_col())
    ax.spines.right.set_visible(ss.is_last_col())
```
