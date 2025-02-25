# Créer une fonction de rappel pour le curseur

Nous allons créer une fonction de rappel qui sera appelée chaque fois que l'utilisateur change les valeurs de seuil à l'aide du curseur. La fonction mettra à jour la carte de couleurs de l'image et les positions des lignes verticales sur l'histogramme.

```python
def update(val):
    # La valeur val passée à un rappel par le RangeSlider sera
    # un tuple de (min, max)

    # Mettez à jour la carte de couleurs de l'image
    im.norm.vmin = val[0]
    im.norm.vmax = val[1]

    # Mettez à jour la position des lignes verticales
    lower_limit_line.set_xdata([val[0], val[0]])
    upper_limit_line.set_xdata([val[1], val[1]])

    # Redessinez la figure pour vous assurer qu'elle est mise à jour
    fig.canvas.draw_idle()


slider.on_changed(update)
```
