# Definir a entrada do menu

Definimos uma função que define a entrada do menu com base no nome do filtro de cores selecionado. Esta função atualiza a função de filtro de cores com base na seleção.

```python
def _set_menu_entry(tb, name):
    tb.canvas.figure.set_agg_filter(_get_color_filter(name))
    tb.canvas.draw_idle()
```
