# Menüeintrag festlegen

Wir definieren eine Funktion, die den Menüeintrag basierend auf dem ausgewählten Namen des Farbfilters festlegt. Diese Funktion aktualisiert die Farbfilterfunktion basierend auf der Auswahl.

```python
def _set_menu_entry(tb, name):
    tb.canvas.figure.set_agg_filter(_get_color_filter(name))
    tb.canvas.draw_idle()
```
