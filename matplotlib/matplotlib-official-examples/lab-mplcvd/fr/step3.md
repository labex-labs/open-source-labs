# Définissez l'entrée du menu

Nous définissons une fonction qui définit l'entrée du menu en fonction du nom du filtre de couleur sélectionné. Cette fonction met à jour la fonction de filtre de couleur en fonction de la sélection.

```python
def _set_menu_entry(tb, name):
    tb.canvas.figure.set_agg_filter(_get_color_filter(name))
    tb.canvas.draw_idle()
```
