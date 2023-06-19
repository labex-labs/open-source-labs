# Set menu entry

We define a function that sets the menu entry based on the selected color filter name. This function updates the color filter function based on the selection.

```python
def _set_menu_entry(tb, name):
    tb.canvas.figure.set_agg_filter(_get_color_filter(name))
    tb.canvas.draw_idle()
```
