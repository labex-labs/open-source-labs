# Establecer la entrada del menú

Definimos una función que establece la entrada del menú basada en el nombre del filtro de color seleccionado. Esta función actualiza la función de filtro de color según la selección.

```python
def _set_menu_entry(tb, name):
    tb.canvas.figure.set_agg_filter(_get_color_filter(name))
    tb.canvas.draw_idle()
```
